from calendar import Calendar     # 导入日历模块中的Calendar类
n=0                               # 初始值
calendar_obj = Calendar()          # 创建默认的Calendar对象
itermonth= calendar_obj.itermonthdays2(2020,8)  # 获取2019年8月份日期对应天数与星期的迭代器
for i in itermonth:               # 循环遍历迭代器中日期对应的天数与星期
    # 月份不等于0且星期为6(即星期日）
    if i[0]!=0 and i[1]==6:
        n=n+1      # 累计求和
        print(i)
print('8月份包含：',n,'个星期日')
