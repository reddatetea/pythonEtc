from datetime import datetime, timezone, timedelta
reduce_four = timezone(timedelta(hours = -6))      # 创建 -6 （西六区）时区对象
plus_four = timezone(timedelta(hours = 9))         # 创建 +9 （东九区——日本东京）时区对象
dt = datetime.now()                                # 获取当前本地日期时间对象
print(dt.astimezone())                             # 打印带有默认的本地的区信息的 datetime 对象
print(dt.astimezone(reduce_four))                  # 设置当前时间为 -6 时区时间
print(dt.astimezone(plus_four))                    # 设置当前时间为 +9 时区时间
