import os  # 文件与操作系统相关模块
if  os.supports_bytes_environ:
    print(os.environb)   # 获取以字节串表示的当前环境变量的映射对象
else:
    print('当前系统不支持os.environb属性！')
