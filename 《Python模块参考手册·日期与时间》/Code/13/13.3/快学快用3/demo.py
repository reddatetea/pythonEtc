import calendar                       #导入日历模块
year=int(input('请输入年份：'))
n=calendar.leapdays(year,year+1)   #检测闰年个数
# 大于零为闰年，否则为平年
if n > 0:
    print('闰年')
else:
    print('平年')
