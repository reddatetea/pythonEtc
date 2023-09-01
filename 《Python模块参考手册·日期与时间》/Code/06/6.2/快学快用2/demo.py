from datetime import time

dtt = time(0, 30, 2, 123456)  # 创建一个时间对象

dtt_micro = dtt.isoformat(timespec="microseconds")  # 精确到微秒
print('精确到微秒：', dtt_micro)
dtt_milli = dtt.isoformat(timespec="milliseconds")  # 精确到毫秒
print('精确到毫秒：', dtt_milli)
dtt_sec = dtt.isoformat(timespec="seconds")  # 精确到秒
print('精确到秒：', dtt_sec)
dtt_min = dtt.isoformat(timespec="minutes")  # 精确到分
print('精确到分：', dtt_min)
dtt_hou = dtt.isoformat(timespec="hours")  # 精确到时
print('精确到时：', dtt_hou)
dtt_auto = dtt.isoformat(timespec="auto")  # 自动
print('自动：', dtt_auto)
