import os  # 文件与操作系统相关模块
handle = open(r'test.txt' ,'r').fileno()  # 获取文件的句柄
print(os.get_handle_inheritable( handle)) # 获取指定句柄的可继承标志
