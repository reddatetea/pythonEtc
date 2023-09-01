import datetime

d1 = datetime.datetime.today()  # 使用今天的日期创建一个日期时间对象
print("今天的日期是：{}".format(d1))
t1 = d1.time()  # 使用日期时间对象创建一个时间对象
print("现在的时间是：{}".format(t1))
t2 = t1.replace(hour=15)  # 替换t1的小时数为15
print("新的时间是：{} ".format(t2))
t3 = t2.replace(fold=1)
print("新的时间是", t3)
