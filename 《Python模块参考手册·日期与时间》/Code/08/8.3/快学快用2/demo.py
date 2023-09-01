import datetime

dt = datetime.datetime.today()  # 获取当前的日期时间
print('当前日期为：', dt)
wd = dt.isoweekday()  # 获取当前星期几（1-7）
rd = 5 - wd  # 计算还剩几天上班的时间
if rd < 0:
    print('您正在休息！')
else:
    # 假设每天的17点下班，生成一个下班的日期时间对象
    tr = dt.replace(hour=17, minute=0, second=0, microsecond=0)
    time_difference = tr - dt  # 时间差
    if time_difference.days == -1:  # 时间超出17点的情况
        print('距离休息还有%s天，请继续加油！' % rd)
    else:  # 时间不到17点的情况
        print('距离休息还有%s天，请继续加油！' % rd, time_difference)
