import sys
print('默认递归次数：',sys.getrecursionlimit()) # 输出默认递归深度
sys.setrecursionlimit(10) # 手动设置递归深度为10
print('修改后递归次数：',sys.getrecursionlimit()) # 输出修改后递归深度
# 定义一个递归函数
def Test(i):
    print('第 {} 次数'.format(i)) # 输出执行次数
    Test(i+1) # 函数递归执行
# 捕获异常信息
try:
    Test(1) # 调用递归函数
except RuntimeError as err: # 捕捉异常
    print(err) # 打印异常信息