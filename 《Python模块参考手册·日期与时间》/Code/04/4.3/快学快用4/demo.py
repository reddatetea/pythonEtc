import random     # 导入随机模块
import time       # 导入时间模块

def random_print(time):
    print('当前间隔时间为：',time )
for i in range(1,6):    # 循环执行5次
    random_time = random.randint(0, 5)    # 产生随机数
    time.sleep(random_time)               # 等待随机时间
    random_print(random_time)             # 执行打印函数
