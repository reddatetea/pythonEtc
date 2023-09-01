import os  # 文件与操作系统相关模块
print(os.getenv('windir', default=None))  # 获取系统环境变量windir的值
print(os.getenv('wind1', default='未定义该环境变量！'))# 获取一个不存在的系统环境变量wind1的值
