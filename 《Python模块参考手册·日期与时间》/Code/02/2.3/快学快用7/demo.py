import time

cur_time = time.time() # 获取当前时间
# 控制程序执行时间在5秒以内
while time.time() - cur_time < 5:
    print('hi')
    time.sleep(1)
