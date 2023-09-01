from calendar import Calendar      # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
for i in range(1,13,1):            # 12个月
    # 获取2020年1至12月对应天数的迭代器
    itermonth= list(calendar_obj.itermonthdays(2020,i))
    # 循环删除列表元素中的0
    while 0 in itermonth:
        itermonth.remove(0)
    # 计算每个月的天数
    print(i,'月：',len(itermonth),'天')
