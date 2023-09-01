import os
print("老王")
print("我是子进程，我的进程号是%d 我的父亲进程是%d"%(os.getpid(),os.getppid()))# 获取子线程和父线程ID
