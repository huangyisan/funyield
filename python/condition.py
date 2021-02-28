import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s',")


def producer(con: threading.Condition):
    logging.debug("Producer thread started")
    # with上下文，自动包含了acquire() and release()方法
    with con:
        logging.debug("Making resource available, sleep 5s")
        # 等待5s。模拟生产
        time.sleep(5)
        logging.debug("Notify all the consumers")
        # 唤醒consumer
        con.notify_all()


def consumer(con: threading.Condition):
    logging.debug("Consumer thread started")
    with con:
        logging.debug("Consumer waiting")
        # wait()方法释放锁，并且进入阻塞等待状态，直到下一次被notify() 或者 notify_all().
        con.wait()
        logging.debug('Consumer consumed the resource')


if __name__ == '__main__':
    # 实例化一个condition
    condition = threading.Condition()

    # producer线程创建
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    # consumer线程创建
    cs_list = []
    cs_num = 5
    for i in range(cs_num):
        cs_list.append(threading.Thread(name='consumer_{}'.format(i), target=consumer, args=(condition,)))

    # consumer线程启动
    for c in cs_list:
        c.start()
        time.sleep(1)

    # producer线程启动
    pd.start()


