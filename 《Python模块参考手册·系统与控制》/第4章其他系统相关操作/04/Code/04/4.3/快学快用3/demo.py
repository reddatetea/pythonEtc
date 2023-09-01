import os  # 文件与操作系统相关模块
import base64  # 导入进行base64编码和解码的模块
result = {}  # 保存生成的随机数的字典
number = 0    # 记录重复次数
for i in range(10000):
    bc = base64.b64encode(os.urandom(3))  # 指定长度为3
    if bc not in result:  # 当不重复时
        result[bc] = 1    # 添加到字典中
    else:
        number +=1  # 重复次数加1
print('重复%d次'%number)
