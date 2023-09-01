import os  # 文件与操作系统相关模块
if os.name == 'nt': # 判断是否为Windows操作系统
    defaultpath =  'D:/python/mr'  # 设置默认路径
elif os.name == 'posix':# 判断是否为Linux/Unix操作系统
    defaultpath = '/home/python/mr' # 设置默认路径
else:
    defaultpath = '未知路径'
print('默认路径为：',defaultpath)  # 输出默认路径
