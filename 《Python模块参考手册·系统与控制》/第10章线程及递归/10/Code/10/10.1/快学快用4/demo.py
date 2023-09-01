import sys
import time # 导入时间模块
import random # 导入随机生成器模块
default=sys.getswitchinterval() # 获取默认线程间隔
i=1 # 定义循环变量
letter = "ABCDEFGHIJKLMNPQRSTUVWXYZ1234567890" # 用于生成序列号的字符串
while True:
    time.sleep(default) # 休眠指定时间
    strone = ''  # 保存生成的单条防伪码，不带横线“-”，循环时清空
    for j in range(25):
        strone = strone + random.choice(letter)  # 每次产生一个随机因子
    # 将生成的防伪码每隔5位添加横线“-”
    strtwo = strone[:5] + "-" + strone[5:10] + "-" + strone[10:15] + "-" + strone[15:20] + "-" + strone[20:25]
    print(strtwo) # 输出执行次数
    i+=1 # 循环变量加1
    if i>10: # 当执行到超过10时
        break # 退出循环