import datetime                                                 # 导入datetime模块
# 创建名称为欧洲 马德里时区
timezone_madrid = datetime.timezone(datetime.timedelta(hours=2),name='Europe/Madrid')
# 创建-4时区
timezone_toronto = datetime.timezone(datetime.timedelta(hours=-4))
t1 = datetime.time(4,5,12,tzinfo=timezone_madrid)      # 马德里时区的时间对象
t2 = datetime.time(4,5,12,tzinfo=timezone_toronto)     # -4时区的时间对象
t3 = datetime.time(4,5,12)      # 未指定时区
print(t1.tzname())
print(t2.tzname())
print(t3.tzname())
