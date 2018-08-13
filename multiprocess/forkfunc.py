import os
print('process {0} start...'.format(os.getpid())) #获取本脚本，的pid
# pid为分叉点，pid给了父进程的同时 也执行后给了子进程，但子进程的pid是在分叉后得到的。
# 父进程fork得到子进程的pid，子进程的fork永远返回0
# 执行的时候先执行父进程
pid = os.fork()
if pid == 0:
    # 子进程执行这条语句
    print('i am child process {0} and my parent is {1}'.format(os.getpid(), os.getppid()))
else:
    print('i {0} just created a child process {1}'.format(os.getpid(), pid))