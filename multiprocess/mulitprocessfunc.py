from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc(name):
    time.sleep(10)
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    # 等待子进程执行完后，在执行join()后面的语句。如果这个代码把join()去掉，那么print('Child process end')还未等子进程结束就执行出来
    # 因为子进程中存在10秒等待。
    p.join()
    print('Child process end.')
