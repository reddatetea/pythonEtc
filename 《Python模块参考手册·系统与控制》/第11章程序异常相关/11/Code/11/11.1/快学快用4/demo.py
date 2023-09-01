import sys
try:
    file=open('test.txt','r') # 打开test.txt文本文件
except:
    types, value, back = sys.exc_info()  # 使用3个变量存储异常类、异常名称及回溯对象
    if types==FileNotFoundError: # 判断异常类名称
        file=open('test.txt','w') # 创建文件