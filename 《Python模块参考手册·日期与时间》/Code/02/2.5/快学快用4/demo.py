import time
t = time.time()    # 获得时间戳
a = time.localtime(t)  # 获得当地时间的时间元组
b = time.gmtime(t)     # 获得UTC时间的时间元组
print('localtime:', a)
print('gmtime   :', b)
