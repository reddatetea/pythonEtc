import datetime

dt0 = datetime.datetime.today()  # 使用今天的日期创建一个日期时间对象
print("今天的日期是：{}".format(dt0), ', 类型为：', type(dt0))

d1 = dt0.date()  # 使用日期时间对象创建一个日期对象
print("现在的日期是：{}".format(d1), ', 类型为：', type(d1))
t2 = dt0.time()  # 使用日期时间对象创建一个时间对象
print("现在的时间是：{}".format(t2), ', 类型为：', type(t2))

t2_hour = t2.replace(hour=15)  # 替换t2的小时数为15
print("新的时间是：{} ".format(t2_hour), ', 类型为：', type(t2_hour))

dt3 = datetime.datetime.combine(d1, t2_hour)  # 组合成一个新的日期时间对象
print("替换后日期是：{}".format(dt3), ', 类型为：', type(dt3))
