import os  # 文件与操作系统相关模块
linesep = os.linesep  # 获取操作系统中分隔行的字符串
print(linesep)  # 直接输出
print('不转义输出：', linesep.encode())   # 编码后输出
