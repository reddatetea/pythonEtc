import datetime

ti = datetime.time(1, 15, 16, 17)  # 创建1小时15分钟16秒17微秒的时间实例
print('ti：', ti, '，类型为：', type(ti))
dtd = datetime.timedelta(hours=-8)  # 使用timedelta创建时区实例
print('dtd：', dtd, '，类型为：', type(dtd))
pst = datetime.timezone(dtd, name="PST")  # 创建一个时区
tl = ti.replace(tzinfo=pst)  # 通过指定时区实例将naive对象转换为aware对象
print('tl：', tl, '，类型为：', type(tl))
