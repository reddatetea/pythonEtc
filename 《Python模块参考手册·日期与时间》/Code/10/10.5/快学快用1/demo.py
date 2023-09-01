import datetime                                                 # 导入datetime模块
reduce_four = datetime.timezone(datetime.timedelta(hours=-4))    # 创建-4时区对象
plus_four = datetime.timezone(datetime.timedelta(hours=4))       # 创建+4时区对象
dt = datetime.datetime.now(reduce_four)                         # 获取-4时区本地日期时间对象
dt1 = datetime.datetime.now(plus_four)                          # 获取+4时区本地日期时间对象
dt2 = datetime.datetime.now()                                   # 获取未设置时区本地日期时间对象
print(dt)                                                       # 打印-4时区本地日期时间
print(dt1)                                                      # 打印+4时区本地日期时间
print(dt2)                                                      # 打印未设置时区本地日期时间
print(dt.utcoffset())                                           # 打印dt对象utc偏移量
print(dt1.utcoffset())                                          # 打印dt1对象utc偏移量
print(dt2.utcoffset())                                          # 打印dt2对象utc偏移量
