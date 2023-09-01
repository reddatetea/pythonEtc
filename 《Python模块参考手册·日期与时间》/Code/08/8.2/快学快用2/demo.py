import datetime

datetime_start = datetime.datetime(year=2020, month=5, day=2)  # 开始日期
datetime_end = datetime.datetime(year=2020, month=5, day=20)  # 结束日期
calendar_start = datetime_start.isocalendar()  # 获取包含周数和星期数的元组
calendar_end = datetime_end.isocalendar()  # 获取包含周数和星期数的元组

if calendar_end[2] >= calendar_start[2]:  # 结束日期的星期数 大 于开始日期的星期数
    week = calendar_end[1] - calendar_start[1]  # 相差几周
    day = calendar_end[2] - calendar_start[2]  # 相差几天
else:  # 结束日期的星期数 小 于开始日期的星期数
    week = calendar_end[1] - calendar_start[1] - 1  # 相差几周，周数减1
    day = calendar_end[2] - calendar_start[2] + 7  # 相差几天，天数加7

date_start = datetime_start.date()  # 开始日期
date_end = datetime_end.date()  # 结束日期
print('%s 与 %s 之间相差了 %d 周 %d 天' % (date_end, date_start, week, day))
