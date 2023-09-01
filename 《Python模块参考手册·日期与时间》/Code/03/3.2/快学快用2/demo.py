import time       # 导入time模块
# 常见时钟方法名称
time_list = ['time','thread_time','process_time','perf_counter','monotonic']
for i in time_list:               # 循环遍历每个时钟方法对应的名称
    print(i,'方法的时钟信息为：\n',time.get_clock_info(i))  # 获取每个时钟方法的信息
