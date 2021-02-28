import threading
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s',")

# resource为公共资源
resource = []
sleep_time = 2


# 定义producer 添加resource
def add_resource(num):
    logging.debug("producer add item {} in resource".format(num))
    time.sleep(sleep_time)
    resource.append(num)


# 定义consumer 消费resource
def consume_resource(re):
    logging.debug("consume from resource")
    logging.debug("consume {}".format(re[0]))
    resource.remove(re[0])


# 定义consumer
def consumer(re, cn: threading.Condition):
    # 获取锁
    cn.acquire()
    while True:
        # 如果消费失败，则调用wait方法，线程睡眠，且释放锁，等待被notify
        try:
            consume_resource(re)
        except:
            logging.debug("resource is empty")
            logging.debug("wait until be notified")
            cn.wait()


def producer(cn: threading.Condition):
    r = random.randint(2, 10)
    logging.debug("random num is {}".format(r))

    for i in range(0, r):
        logging.debug("produce item, add {} in resource in 2s".format(i))
        time.sleep(sleep_time)

        logging.debug("try to get lock")
        # 获取锁
        cn.acquire()

        try:
            # 尝试添加资源。并且通知所有其他线程
            add_resource(i)
            cn.notify_all()
        # 无论如何最终都释放锁
        finally:
            cn.release()


if __name__ == '__main__':
    con = threading.Condition()
    pd = threading.Thread(name="producer", target=producer, args=(con,))

    cs_list = []
    cs_num = 3
    for i in range(1, cs_num):
        cs_list.append(threading.Thread(name="cs_{}".format(i), target=consumer, args=(resource, con,)))

    for c in cs_list:
        c.start()
        time.sleep(sleep_time)

    pd.start()

