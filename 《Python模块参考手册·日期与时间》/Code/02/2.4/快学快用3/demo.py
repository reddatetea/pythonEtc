import time

a = "2020-10-01 23:40:00"  # 指定时间
time_array = time.strptime(a, "%Y-%m-%d %H:%M:%S")  # 将其转换为时间数组
print('时间元组', time_array)
time_stamp = time.mktime(time_array)  # 转换为时间戳
print('时间戳', time_stamp)
time_gt = time.gmtime(time_stamp)  # 转换为时间元组
print('时间元组', time_gt)
