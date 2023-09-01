import datetime                                                 # 导入datetime模块
# 创建名称为欧洲 马德里时区
timezone_madrid = datetime.timezone(datetime.timedelta(hours=2),name='Europe/Madrid')
# 创建-4时区
timezone_toronto = datetime.timezone(datetime.timedelta(hours=-4))
print(timezone_madrid.utc)              # 打印欧洲 马德里时区的utc时区
print(timezone_toronto.utc)             # 打印-4时区的utc时区
