import time
now = time.time()  # 获取当前时间戳
print(now)
now_str = time.ctime(now)  # 转换为字符串
print(now_str)
time_array = time.strptime(now_str)  # 转换为时间数组
print(time_array)
now_mkt = time.mktime(time_array)  # 转换为时间戳
print(now_mkt)
