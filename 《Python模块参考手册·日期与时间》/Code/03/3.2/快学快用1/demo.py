import time       # 导入time模块
time_namespace = time.get_clock_info('time')  # 获取time()方法的时钟信息
print(time_namespace)
