from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
itermonth= calendar_obj.itermonthdays2(2019,8)  # 获取2019年8月份日期对应天数与星期的迭代器
for i in itermonth:               # 循环遍历迭代器中日期对应的天数与星期
    # 打印迭代器中日期对应的天数与星期，其中代表星期的数字0表示星期1,数字6表示星期日
    print(i)
