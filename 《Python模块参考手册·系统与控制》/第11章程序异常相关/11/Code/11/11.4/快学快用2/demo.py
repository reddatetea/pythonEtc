import sys
sys.tracebacklimit=0 # 设置最大递归（回溯）层级为0级
# sys.tracebacklimit=1 # 设置最大递归（回溯）层级为1级
try:
    file=open('test.txt','r') # 打开test.txt文本文件
except:
    types, value, back = sys.exc_info()  # 捕获异常
    sys.excepthook(types, value, back)  # 打印异常