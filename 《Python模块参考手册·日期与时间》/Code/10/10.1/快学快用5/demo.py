from datetime import datetime    # 导入 datetime 模块中的 datetime 类
from datetime import timedelta   # 导入 datetime 模块中的 timedelta 类

# 创建 datetime 时间对象
now = datetime(year = 2020, month = 6, day = 26, \
               hour = 16, minute = 30, second = 50, \
               microsecond = 1000 * 999)
# 创建一个 时间段 对象
delta = timedelta(days = 1)
# 计算将一个时间点倒退一天的具体时间
before = now - delta
#  或者为
before_02 = now.replace(day = now.day - 1)
print(f"before == before_02 : {before == before_02}")
print("    原来的时间点为：", now)
print(f"倒退一天的时间点为：", before)
