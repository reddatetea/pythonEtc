import sys
def add(a,b): # 定义一个函数，用来计算两个数的和
    return a+b # 返回值为两个数的和
# 使用sys.call_tracing调用定义的add函数，并传入相应的参数
result = sys.call_tracing(add,(3,4))
print(result) # 输出结果