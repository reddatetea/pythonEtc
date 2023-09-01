import datetime                                                 # 导入datetime模块
reduce_four = datetime.timezone(datetime.timedelta(hours=-4))    # 创建-4时区对象
plus_four = datetime.timezone(datetime.timedelta(hours=4))       # 创建+4时区对象
t1 = datetime.time(13,57,12,tzinfo=reduce_four)                   # -4时区time对象
t2 = datetime.time(13,57,12,tzinfo=plus_four)                     # +4时区time对象
t3 = datetime.time(13,57,12)                                      # 未设置时区time对象
print(t1.utcoffset())                                             # 打印t1对象utc偏移量
print(t2.utcoffset())                                             # 打印t2对象utc偏移量
print(t3.utcoffset())                                             # 打印t3对象utc偏移量
