import datetime       # 导入日期时间模块
import time           # 导入时间模块

def spider():
    # 模拟爬虫函数
    print('爬虫程序执行中。。。。')

def timing(h,m):                               # 创建定时函数
    while True:
        now = datetime.datetime.now()           # 获取当前时间
        if now.hour == h and now.minute == m:   # 如果当前时间为定时时间
            spider()                             # 启动爬虫函数
        time.sleep(60)                           # 每60秒（1分钟）检测一次
timing(14,59)                                    # 调用定时函数，并设置时间为14:59分
