import os  # 文件与操作系统相关模块
import base64  # 导入进行base64编码和解码的模块
key = os.urandom(32) 
print(base64.b64encode(key)) # 进行base64编码
