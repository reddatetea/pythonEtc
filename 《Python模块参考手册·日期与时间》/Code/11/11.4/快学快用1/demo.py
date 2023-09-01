import datetime                                                 # 导入datetime模块
# 创建名称为欧洲 马德里时区
timezone_madrid = datetime.timezone(datetime.timedelta(hours=2),name='Europe/Madrid')
dt = datetime.datetime.now(tz=timezone_madrid) # 指定马德里时区的datetime对象
print(dt)                                         # 打印马德里当前时间
print(timezone_madrid.fromutc(dt))              # 打印包含datetime+offset信息的datetime对象
