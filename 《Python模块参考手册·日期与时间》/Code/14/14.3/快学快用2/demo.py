from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
itermonth= calendar_obj.itermonthdays4(2020,8)  # 获取2020年8月的年、月、日、星期数字
days=0                            # 初始工作日天数
for i in itermonth:               # 循环遍历迭代器中的（年、月、日、星期数字）
    if i[1]==8:                   # 仅保留8月份
        if i[3]!=5 and i[3]!=6:   # 除去星期六和星期日
            days=days+1           # 累计求和（8月份的工作日）
print('2020年8月份的工作日是：',days,'天')
