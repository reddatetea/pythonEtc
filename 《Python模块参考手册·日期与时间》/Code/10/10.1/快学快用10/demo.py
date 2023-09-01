from datetime import datetime    # 导入 datetime 模块中的 datetime 类
from datetime import timedelta   # 导入 datetime 模块中的 timedelta 类
import calendar

# 创建 datetime 时间对象
date_dict = {"year": 2020, "month" : 2, "day" : 29, \
               "hour": 22, "minute": 8, "second" : 20, \
               "microsecond":  1000 * 30}
now = datetime(**date_dict)
days = 365
# 判断未来一年份是否是闰年
after_leap = calendar.isleap(now.year + 1)
# 判断当前年份是否是闰年
now_leap = calendar.isleap(now.year)
date_dict["month"], date_dict['day'] = 2, 28
if now_leap:
    # 当前年份若是闰年， 再判断是否 小于等于 2 月 28 号
    if now <= datetime(**date_dict):
        days = 366
elif after_leap:
    # 未来一年份若是闰年， 再判断是否 大于2 月 28 号
    if now > datetime(**date_dict):
        days = 366
# 根据上一年份的天数创建 timedelta 对象
month_delta = timedelta(days = days)
# 计算将一个时间点快进一年的具体时间
after = now + month_delta
print("    原来的时间点为：", now)
print(f"快进一年的时间点为：", after)
