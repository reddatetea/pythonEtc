import os  # 文件与操作系统相关模块
r,w = os.pipe()  # 创建用于读写的文件描述符
os.set_handle_inheritable( w ,False) # 设置指定句柄的不可继承标志
print(os.get_handle_inheritable( w)) # 获取指定句柄的可继承标志