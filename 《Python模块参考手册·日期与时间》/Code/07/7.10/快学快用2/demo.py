import datetime

datetime_start = datetime.datetime(year=2020, month=2, day=2)  # 开始日期
datetime_end = datetime.datetime(year=2020, month=5, day=20)  # 结束日期
days_start = datetime_start.toordinal()  # 获取开始日期的天数
print('days_start:', days_start)
days_end = datetime_end.toordinal()  # 获取结束日期的天数
print('days_end:', days_end)
days = days_end - days_start  # 两个日期天数差
print('两个日期相差 %d 天' % days)
