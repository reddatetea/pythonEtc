import sys # 导入模块
import time # 导入时间模块
default=sys.getswitchinterval() # 获取默认线程间隔
i=1 # 定义循环变量
while True:
    time.sleep(default) # 休眠指定时间
    print('第%d次执行'%i) # 输出执行次数
    i+=1 # 循环变量加1
    if i==10: # 当执行到第10次时
        break # 退出循环