from calendar import Calendar      # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
for i in range(2010,2021,1):            # 2010年至2020年
    # 获取2010年至2020年每年2月日期对应的迭代器
    itermonth= list(calendar_obj.itermonthdays(i,2))
    # 循环删除列表元素中的0
    while 0 in itermonth:
        itermonth.remove(0)
    # 计算每年2月份的天数
    print(i,'年2月：',len(itermonth),'天')
