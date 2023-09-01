import sys
try:
    file=open('test.txt','r') # 打开test.txt文本文件
except:
    print(sys.exc_info())  # 捕获并输出异常相关信息