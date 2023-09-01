import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDWR)  # 打开文件描述符
print(os.isatty(fd))  # 输出是否连接到类似TTY设备
os.close(fd)    # 关闭文件描述符
