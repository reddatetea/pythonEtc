import os  # 文件与操作系统相关模块
# 当第三方模块未安装时
try:
    import numpy  # 导入模块
except ModuleNotFoundError:  # 处理异常
    print('正在安装Numpy模块，请稍等......')
    os.sytem('pip install numpy')  # 安装模块
