import sys
list =sys.thread_info # 获取线程信息
if list[1]=='semaphore': # 判断锁的名称
    print('锁使用信号量')
elif list[1]=='mutex+cond':
    print('锁使用互斥锁和条件变量')
else:
    print('未知')