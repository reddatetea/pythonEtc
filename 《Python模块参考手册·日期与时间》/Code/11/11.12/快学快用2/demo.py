from datetime import timezone, timedelta
from datetime import datetime

obj = datetime(2020, 12, 23, 20, 20, 20 )
# 设置 UTC 标准时区
obj = obj.replace(tzinfo = timezone.utc)

# 创建一个新的时区
tz_obj = timezone(timedelta(hours = 9))  # 东 9 区 （日本东京）
# 时区转换
obj = obj.astimezone(tz_obj)
print(f"转换为东京的时间为：  {obj}")
