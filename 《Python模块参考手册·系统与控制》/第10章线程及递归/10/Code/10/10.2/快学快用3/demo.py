import sys
import time # 导入时间模块
import random # 导入随机生成器模块
sys.setswitchinterval(1) # 设置线程间隔
default=sys.getswitchinterval() # 获取设置的线程间隔
number = "1234567890" # 用于生成防伪码的数字集合
for m in range(int(10)):  # 分类产品编号
    time.sleep(default)  # 休眠指定时间
    randfir = ''
    for i in range(6):  # 生成一个不包含类别的产品防伪码
        randfir = randfir + random.choice(number)  # 每次生成一个随机因子
    print(str(int(201) + m) + randfir)  # 将生成的单条防伪码添加到防伪码列表