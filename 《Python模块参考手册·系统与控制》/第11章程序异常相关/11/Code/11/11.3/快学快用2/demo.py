import sys
try:
    file=open('test.txt','r') # 打开test.txt文本文件
except:
    types, value, back = sys.exc_info()  # 捕获异常
    sys.excepthook(types, value, back)  # 打印异常