from datetime import datetime    # 导入 datetime 模块中的 datetime 类
from datetime import timedelta   # 导入 datetime 模块中的 timedelta 类

# 创建 datetime 时间对象
now = datetime(year = 2020, month = 5, day = 16, \
               hour = 6, minute = 10, second = 20, \
               microsecond = 1000 * 1)
# 创建一个 时间段 对象
delta = timedelta(days = 1)
# 计算将一个时间点快进一天的具体时间
after = now + delta
# 等价于
after_02 = now.replace(day = now.day + 1)
print(f"after == after_02 : {after == after_02}")
print("    原来的时间点为：", now)
print(f"快进一天的时间点为：", after)
