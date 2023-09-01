import sys
sys.setrecursionlimit(1500) # 设置递归调用值为1500
def count(num): # 定义函数，用来递归调用
    print(num) # 输出数字
    num+=1 # 数字加1
    if num<1000: # 判断数字小于1000，则递归调用
        count(num)
    else: # 否则弹出提示信息
        print('递归超出限制！')
count(0) # 调用函数