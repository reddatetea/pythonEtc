from datetime import datetime    # 导入 datetime 模块中的 datetime 类
from datetime import timedelta   # 导入 datetime 模块中的 timedelta 类
from calendar import monthrange  # 导入 日历 模块中的 月份迭代器

# 创建 datetime 时间对象
now = datetime(year = 2020, month = 6, day = 6, \
               hour = 14, minute = 18, second = 40, \
               microsecond = 1000 * 10)

# 计算当前所在月份的下一月份的天数 (星期几， 天数)： 0 为星期一
after_month_days = monthrange(now.year, now.month + 1)
# 根据下一月份的天数创建 timedelta 对象
month_delta = timedelta(days = after_month_days[1])
# 计算将一个时间点快进一个月的时间
after = now + month_delta
print("      原来的时间点为：", now)
print(f"快进一个月的时间点为：", after)
print(f"且下一个月的今天为：星期 {after.isoweekday()}")
