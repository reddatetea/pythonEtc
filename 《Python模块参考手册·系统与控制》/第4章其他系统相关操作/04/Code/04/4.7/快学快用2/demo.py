import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt', os.O_RDWR)  # 打开文件描述符
if os.get_inheritable(fd):# 判断文件描述符的可继承标志为True
    print("此文件描述符是可继承标志")  # 提示
else:# 判断文件描述符的可继承标志为False
    print("此文件描述符是不可继承标志")  # 提示
os.close(fd)    # 关闭文件描述符
