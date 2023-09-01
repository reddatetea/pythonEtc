import time                    # 导入时间模块
t = time.time()                # 获取当前时间的时间戳
time_tup = time.localtime(t)    # 将时间戳转换为时间元组
print(time_tup.tm_year)         # 当前年份
print(time_tup.tm_mon)          # 月份
print(time_tup.tm_mday)         # 日
print(time_tup.tm_hour)         # 时
print(time_tup.tm_min)          # 分
print(time_tup.tm_sec)          # 秒
