import os  # 文件与操作系统相关模块
if os.name == 'posix':  # 如果是Unix操作系统
    tempname = '/home/python/mr'
    mode = ((os.stat(tempname).st_mode)|0o555) & 0o777
    os.chmod(tempname,mode)    # 设置路径模式
elif os.name == 'nt':
    import stat  # 导入stat模块
    tempname = 'D:/temp/mr'
    os.chmod(tempname,stat.S_IREAD)  # 将路径模式更改为读模式
