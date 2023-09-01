import calendar                                  #导入日历模块
#将时间元组转换为时间戳
date_start=calendar.timegm((2020,5,21,0,0,0))   # 当前时间
date_end=calendar.timegm((2021,6,7,0,0,0))   # 2021年高考时间：2021年6月7日
#1天=86400 秒
print('距离2021年高考：',int((date_end-date_start)/86400),'天')
