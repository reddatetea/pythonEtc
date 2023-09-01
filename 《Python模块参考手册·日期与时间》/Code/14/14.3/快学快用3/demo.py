from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
# itermonthdays()方法
itermonth= calendar_obj.itermonthdays(2019,8)  # 2019年8月的日期迭代器
for i in itermonth:               # 循环遍历迭代器
    print(i)                      # 输出日期对应的天数
# itermonthdays2()方法
itermonth2 = calendar_obj.itermonthdays2(2019, 8)  # 2019年8月的日期迭代器
for i2 in itermonth2:  # 循环遍历迭代器
    print(i2)  # 输出日期对应的天数和星期
itermonth3= calendar_obj.itermonthdays3(2019,8)  # 2019年8月的日期迭代器
# itermonthdays3()方法
for i3 in itermonth3:               # 循环遍历迭代器
    print(i3)                      # 输出日期对应的年、月、日
# itermonthdays4()方法
itermonth4= calendar_obj.itermonthdays4(2019,8)  # 2019年8月的日期迭代器
for i4 in itermonth4:               # 循环遍历迭代器
    print(i4)                      # 输出日期对应的年、月、日和星期
