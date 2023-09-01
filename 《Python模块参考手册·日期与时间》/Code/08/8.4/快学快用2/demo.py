import datetime

dt = datetime.date.today()  # 获取当前的日期
print('当前日期为：', dt)
wd = dt.isoweekday()  # 获取当前星期几（1-7）
rd = 5 - wd  # 计算还剩几天上班的时间
if rd < 0:
    print('您正在休息！')
else:
    print('还剩%d天休息！' % rd)
