import time                   # 导入time模块
t=time.localtime()            # 获取本地当前时间的时间元组
print('本地当前时间的时间元组为：',t)                       # 输出本地当前时间的时间元组
print('返回的时间戳为：',time.mktime(t))          # 以本地当前时间的时间元组为参数返回时间戳
