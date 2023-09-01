import sys
try:
    print(1 / 0)
except:
    print(sys.exc_info())  # 捕获并输出异常相关信息