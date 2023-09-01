import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt', os.O_RDWR)  # 打开文件描述符
os.set_inheritable(fd,False)  # 设置fd可继承
print(os.get_inheritable(fd))  # 输出fd是否可继承
os.close(fd)  # 关闭文件描述符
