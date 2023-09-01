import calendar                    # 导入日历模块
from calendar import Calendar      # 导入日历模块中的Calendar类
mydate_list=[]                     # 创建列表
calendar_obj = Calendar()          # 创建默认的Calendar对象
# 循环获取2020年5月至7月的日期迭代器
for i in range(5,8,1):
    itermonth = calendar_obj.itermonthdates(2020, i)
    # 循环遍历迭代器中的日期（其中包含当前月份开始那周与结束那周的所有日期）
    for date in itermonth:
        # 日期转换为列表
        date_list = list(map(int,str(date).split('-')))
        # 获取指定日期的星期码
        n=calendar.weekday(date_list[0],date_list[1],date_list[2])
        # 去除日期中包含的4月和8月的日期
        if  date_list[1]!=4 and date_list[1]!=8:
            # 去除星期六、星期日和重复的日期添加到列表中
            if n != 5 and n != 6:
                if str(date) not in mydate_list: #去除重复日期
                    mydate_list.append(str(date))
print('计划日期如下：')
print(mydate_list)
print('计划工作日：',len(mydate_list),'天')
