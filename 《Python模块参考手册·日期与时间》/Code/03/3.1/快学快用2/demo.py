import time

time_s = time.time()  # 获取当前系统时间
mono_s = time.monotonic()  # 获取单调时间
print('请手动更改系统时间！')
time.sleep(10)  # 程序睡眠10秒钟，此时需要手动改变系统的时间
time_e = time.time()
mono_e = time.monotonic()
print('系统时间', time_e - time_s)
print('单调时间', mono_e - mono_s)
