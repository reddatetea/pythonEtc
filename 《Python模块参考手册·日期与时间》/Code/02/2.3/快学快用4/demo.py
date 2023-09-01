import time
flag = input('按下回车开始计时：')
try:
    time_start = time.time()
    while True:
        time_end = time.time()  # 获取当前时间戳
        t = time_end - time_start
        print('\r', '%f秒' % t, end="")  # 动态刷新控制台
except KeyboardInterrupt:
    print('计时结束，共用时%f秒', t)
