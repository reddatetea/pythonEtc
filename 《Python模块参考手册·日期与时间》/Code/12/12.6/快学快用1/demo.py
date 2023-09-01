import calendar,time                                  #导入日历模块和时间模块
#将时间元组转换为时间戳
print('指定时间元组对应的时间戳为：',calendar.timegm((2019,1,2,21,26,0,0,0,0)))
#将localtime()方法获取的当前时间的时间元组转换为时间戳
print('当前时间元组对应的时间戳为：',calendar.timegm(time.localtime()))
