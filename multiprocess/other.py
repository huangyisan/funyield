from multiprocessing import Process
import time

def A():
    while True:
        print('正在调用函数')
        time.sleep(1)
p = Process(target = A)
p.start()