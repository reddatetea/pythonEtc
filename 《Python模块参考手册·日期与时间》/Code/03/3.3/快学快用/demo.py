import time           # 导入time模块
start_time = time.monotonic_ns()    # 第一次调用
time.sleep(2)                    # 休眠2秒
end_time = time.monotonic_ns()      # 第二次调用
print('第一次返回的单调时钟纳秒值为：',start_time)
print('第二次没回的单调时钟纳秒值为：',end_time)
print('计算休眠时间的纳秒为：',end_time-start_time)
