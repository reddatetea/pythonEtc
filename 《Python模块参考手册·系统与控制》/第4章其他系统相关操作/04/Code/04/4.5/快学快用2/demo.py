import os                                 # 文件与操作系统相关模块
handle = open(r'test.txt' ,'r').fileno()  # 获取文件的句柄
if os.get_handle_inheritable( handle):    # 判断指定句柄的可继承标志为True
    print("此句柄是可继承标志")           # 提示
else:                                     # 判断指定句柄的可继承标志为False
    print("此句柄是不可继承标志")         # 提示
