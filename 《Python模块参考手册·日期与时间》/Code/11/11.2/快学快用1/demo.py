import datetime                                                 # 导入datetime模块
from dateutil.tz import gettz                                   # 导入获取指定时区的方法
dt1 = datetime.datetime.now(tz=gettz('China Standard Time'))       # 获取中国标准时间时区
dt2 = datetime.datetime.now(tz=gettz('Pacific/Kiritimati'))       # 获取太平洋 圣诞岛时区
dt3 = datetime.datetime.now(tz=gettz('Australia/Sydney'))         # 澳大利亚   悉尼时区
dt4 = datetime.datetime.now(tz=gettz('Europe/Madrid'))            # 获取欧洲   马德里时区
dt5 = datetime.datetime.now(tz=gettz('America/Toronto'))          # 获取美国   多伦多时区
print('中国标准时间时区:',dt1)
print('夏令时偏移量：',dt1.dst())
print('太平洋 圣诞岛时区:',dt2)
print('夏令时偏移量：',dt2.dst())
print('澳大利亚 悉尼时区:',dt3)
print('夏令时偏移量：',dt3.dst())
print('欧洲 马德里时区',dt4)
print('夏令时偏移量：',dt4.dst())
print('美国 多伦多时区',dt5)
print('夏令时偏移量：',dt5.dst())
