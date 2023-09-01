import datetime

today = datetime.date.today()  # 获取今天的日期
week_day = today.isoweekday()  # 获取今天是星期几
day = datetime.datetime.today().day  # 获取今天是几号
date_str = datetime.datetime.today().strftime("%Y-%m-%d, %A")  # 转换为字符串
# 如果 为星期1并且日期为1-3号之间 或 日期为1号并且星期在2-5之间 就认为是每月的第一个工作日
if (week_day == 1 and day in (1, 2, 3)) or (week_day in (2, 3, 4, 5) and day == 1):
    print("今天：{0} 是每月的第一个工作日。".format(date_str))
else:
    print("今天：{0} 不是每月的第一个工作日。".format(date_str))
