import datetime

stamp_start = 1589945012.5059443
stamp_end = 1589946088.5059666
stamp = stamp_end - stamp_start
print('stamp：', stamp)
a = datetime.datetime.fromtimestamp(stamp)  # 相差的时间戳 日期时间
b = datetime.datetime.fromtimestamp(0)  # 公历开始时间
c = a - b  # 日期时间差
print('相差的时间为：', c)
