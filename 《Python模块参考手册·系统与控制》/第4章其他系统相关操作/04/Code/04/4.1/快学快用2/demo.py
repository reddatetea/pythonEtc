import os  # 文件与操作系统相关模块
for i in range(1,21):
    print('错误码 %d：' %i,os.strerror(i))  # 输出错误码对应的错误信息
