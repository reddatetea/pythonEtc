import os  # 文件与操作系统相关模块
if os.supports_bytes_environ:# 原生环境类型是字节型
      print('当前系统不是Windows系统')# 则不是Windows系统
else:# 原生环境类型不是字节型
    print('当前系统是Windows系统')# 则是Windows系统
