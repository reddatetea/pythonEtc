import datetime                                                 # 导入datetime模块
from dateutil.tz import gettz                                   # 导入获取指定时区的方法
dt1 = datetime.datetime.now(tz=gettz('China Standard Time'))       # 获取中国标准时间时区
dt2 = datetime.datetime.now(tz=gettz('Pacific/Kiritimati'))       # 获取太平洋 圣诞岛时区
dt3 = datetime.datetime.now(tz=gettz('Australia/Sydney'))         # 澳大利亚   悉尼时区
dt4 = datetime.datetime.now(tz=gettz('Europe/Madrid'))            # 获取欧洲   马德里时区
dt5 = datetime.datetime.now(tz=gettz('America/Toronto'))          # 获取美国   多伦多时区
dt6 = datetime.datetime.now()                                     # 未指定时区
print('中国标准时间时区名称:',dt1.tzname())
print('太平洋 圣诞岛时区名称:',dt2.tzname())
print('澳大利亚 悉尼时区名称:',dt3.tzname())
print('欧洲 马德里时区名称：',dt4.tzname())
print('美国 多伦多时区名称',dt5.tzname())
print('未指定时区：',dt6.tzname())
