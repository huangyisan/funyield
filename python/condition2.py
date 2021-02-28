import threading
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s',")

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
    cn.acquire()
    while True:
        try:
            consume_resource(re)
        except:
            logging.debug("resource is empty")
            logging.debug("wait until be notified")
            cn.wait()


def producer(cn: threading.Condition):
    r = random.randint(2, 4)
    logging.debug("random num is {}".format(r))

    for i in range(0, r):
        logging.debug("produce item, add {} in resource in 2s".format(i))
        time.sleep(sleep_time)

        logging.debug("try to get lock")
        cn.acquire()

        try:
            add_resource(i)
            cn.notify_all()
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

    pd.join()
    c.join()
