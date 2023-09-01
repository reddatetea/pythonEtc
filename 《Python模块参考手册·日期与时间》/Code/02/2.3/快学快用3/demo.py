import time  # 导入时间模块
start_time = time.time()  # 记录开始时间
for i in range(1000001):  # 循环输出0~1000000
    print(i)
end_time = time.time()  # 记录结束时间
run_time = end_time - start_time  # 计算运行时间
print('运行时间: ', run_time)  # 输出运行时间
