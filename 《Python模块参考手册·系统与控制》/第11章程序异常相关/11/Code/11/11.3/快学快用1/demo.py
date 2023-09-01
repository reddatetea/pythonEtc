import sys
try:
    result = 1 / 0
except:
    types, value, back = sys.exc_info()  # 捕获异常
    sys.excepthook(types, value, back)  # 打印异常