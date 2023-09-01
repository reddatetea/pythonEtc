import datetime

date_bir = datetime.date(1996, 8, 2)  # 出生日期
date_now = datetime.date.today()  # 当前日期

bir_days = date_bir.toordinal()  # 出生日期到0001-01-01的天数
now_days = date_now.toordinal()  # 当前日期到0001-01-01的天数

days = now_days - bir_days
print('您已存活了 %d 天' % days)
