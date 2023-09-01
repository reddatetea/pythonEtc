import datetime                                                 # 导入datetime模块
reduce_four = datetime.timezone(datetime.timedelta(hours=-4))    # 创建-4时区对象
plus_four = datetime.timezone(datetime.timedelta(hours=4))       # 创建+4时区对象
dt1 = datetime.datetime.now()                                    # 获取未设置时区本地日期时间对象
dt2 = datetime.datetime.now(reduce_four)                         # 获取-4时区本地日期时间对象
dt3 = datetime.datetime.now(plus_four)                           # 获取+4时区本地日期时间对象
print(dt1.timetuple())                  # 打印未设置时区的时间元组,默认北京时区+8
print(dt1.utctimetuple())               # 打印未设置时区UTC协调世界时的时间元组,默认北京时区+8
print(dt2.timetuple())                  # 打印-4时区的时间元组，tm_hour=当前小时-8-4
print(dt2.utctimetuple())               # 打印-4时区UTC协调世界时的时间元组，tm_hour=当前小时-8
print(dt3.timetuple())                  # 打印+4时区的时间元组，tm_hour=当前小时-4
print(dt3.utctimetuple())               # 打印+4时区UTC协调世界时的时间元组，tm_hour=当前小时-8
