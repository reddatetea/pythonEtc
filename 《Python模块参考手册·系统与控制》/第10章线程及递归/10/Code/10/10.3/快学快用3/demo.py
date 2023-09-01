import sys
list =sys.thread_info # 获取线程信息
if list[0]=='nt': # 判断name名称
    print('当前为Windows线程')
elif list[0]=='pthread':
    print('当前为POSIX线程')
elif list[0]=='solaris':
    print('当前为Solaris线程')