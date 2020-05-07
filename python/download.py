import requests
import urllib
import os
import asyncio
import logging
from logging import handlers
from tqdm import tqdm


class Logger:
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }
    # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)# 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))# 设置日志级别
        sh = logging.StreamHandler() # 往屏幕上输出
        sh.setFormatter(format_str) # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)# 设置文件里写入的格式
        self.logger.addHandler(sh) # 把对象加到logger里
        self.logger.addHandler(th)


class Music:
    def __init__(self, name, type_str):
        self.name = name
        self.type_str = type_str
        self.url = "https://music.liuzhijin.cn"
        self.headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Origin": "https://music.liuzhijin.cn",
        "Referer": f"https://music.liuzhijin.cn/?name={urllib.parse.quote(name)}&type={type_str}",
        "Content-length": "60",
        "x-requested-with": "XMLHttpRequest",
        "Content-type":"application/x-www-form-urlencoded; charset=UTF-8"
    }

    def post(self, page=1):
        items = {"input": self.name,
                 "filter": "name",
                 "type": self.type_str,
                 "page": page}
        log.logger.info(self.url)
        res_post = requests.post(url=self.url, headers=self.headers, data=items)

        data = res_post.json()["data"]
        return data

    def downloading(self, url, music_name):
        """
        开始下载
        :param url:
        :param music_name:
        :return:
        """
        res = requests.get(f"{url}")
        chunk_size = 1024
        dirs = f"{self.name}"
        if not os.path.exists(f"{dirs}"):
            os.mkdir(f"{dirs}")
        filename = music_name.replace(" ",'')
        filename = filename.split("（")[0]
        with open(f"{dirs}/{filename}.mp3", 'wb') as f:
            for data in res.iter_content(chunk_size=chunk_size):
                f.write(data)

    async def run(self, urls):

        urls_data = map(lambda x:(x["url"], x["title"]),urls)
        for url, music_name in urls_data:
            log.logger.info(f'{music_name}-{url}')
            if url:
                self.downloading(url, music_name)

    async def main(self, number):
        """
        主方法
        """
        task_list = [self.post(x) for x in range(1, 2)]
        task_number = len(task_list)
        # 划分任务
        async_number = [task_list[i:i + number] for i in range(0, task_number, number)]
        tasks_result = []
        pbar = tqdm(total=len(async_number))
        for urls in async_number:
            tasks = [asyncio.ensure_future(self.run(url)) for url in urls]
            for task in asyncio.as_completed(tasks):
                result = await task
                tasks_result.append(result)
            pbar.update()
        log.logger.info("爬取完成")


if __name__ == '__main__':

    log = Logger('all.log', level='info')
    log.logger.info('info')
    music = Music("周杰伦","netease")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(music.main(10))
