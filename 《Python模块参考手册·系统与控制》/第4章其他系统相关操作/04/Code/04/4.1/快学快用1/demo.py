import os  # 文件与操作系统相关模块
print('错误码 2对应的错误信息：',os.strerror(2))  # 错误码2对应的错误信息
print('错误码 10对应的错误信息：',os.strerror(10))  # 错误码10对应的错误信息
no = int(input('请输入错误码：'))  # 输入错误码
print('错误码%d对应的错误信息：%s'%(no,os.strerror(no)))  # 获取并输出输入的错误码对应的错误信息
