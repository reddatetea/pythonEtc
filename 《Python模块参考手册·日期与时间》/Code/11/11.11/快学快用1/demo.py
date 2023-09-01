import datetime                                                 # 导入datetime模块
# 创建名称为欧洲 马德里时区
timezone_madrid = datetime.timezone(datetime.timedelta(hours=2),name='Europe/Madrid')
reduce_four = datetime.timezone(datetime.timedelta(hours=-4))    # 创建-4时区对象
plus_four = datetime.timezone(datetime.timedelta(hours=4))       # 创建+4时区对象
utc_time = datetime.timezone(datetime.timedelta(hours=0))     # 创建utc时区对象，协调世界时为0
dt = datetime.datetime.now()              # datetime对象
print(timezone_madrid.utcoffset(dt))      # 打印时区名称
print(reduce_four.utcoffset(dt))          # 打印-4时区
print(plus_four.utcoffset(dt))            # 打印+4时区
print(utc_time.utcoffset(dt))             # 打印utc时区
