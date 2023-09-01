import datetime                                                 # 导入datetime模块
# 创建名称为欧洲 马德里时区
timezone_madrid = datetime.timezone(datetime.timedelta(hours=2),name='Europe/Madrid')
reduce_four = datetime.timezone(datetime.timedelta(hours=-4))    # 创建-4时区对象
dt = datetime.datetime.now(reduce_four)                     # 创建一个使用-4时区的datetime对象
dt1 = datetime.datetime.now()                                 # 未指定时区的datetime对象
print(timezone_madrid.dst(dt))                              # 打印自定义欧洲 马德里时区对象的dst
print(timezone_madrid.dst(dt1))                             # 打印自定义欧洲 马德里时区对象的dst
