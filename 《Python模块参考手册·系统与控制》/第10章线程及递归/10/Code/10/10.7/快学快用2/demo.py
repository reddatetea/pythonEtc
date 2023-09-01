import sys
def show(): # 定义一个函数，用来显示信息
   print('敢想敢为  注重细节')
# 使用sys.call_tracing调用定义的show函数
result = sys.call_tracing(show,())
print(result) # 输出结果