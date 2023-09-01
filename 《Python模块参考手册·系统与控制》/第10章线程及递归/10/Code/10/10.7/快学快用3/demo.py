import sys
def show(): # 定义一个函数，用来返回一个列表
   return ['做深','做专','做到位']
# 使用sys.call_tracing调用定义的show函数
result = sys.call_tracing(show,())
print(result) # 输出结果