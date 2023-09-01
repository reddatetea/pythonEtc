import calendar                # 导入日历模块
import datetime                # 导入日期时间模块
mytime=datetime.datetime.now()   # 当前系统时间
y=mytime.year      # 年
m=mytime.month     # 月
d=mytime.day       # 日
h=mytime.hour      # 小时
min=mytime.minute  # 分钟
s=mytime.second    # 秒
#将时间元组转换为时间戳
a=calendar.timegm((y,m,d,h,min,s))   # 当前时间
print('10位时间戳：',a)
#通过将秒乘以1000转换为毫秒的方法获取13位时间戳
print('13位时间戳：',a*1000)
