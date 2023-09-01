from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
itermonth= calendar_obj.itermonthdays4(2019,8)  # 获取2019年8月的年、月、日、星期数字
for i in itermonth:               # 循环遍历迭代器中的（年、月、日、星期数字）
    print(i)                      # 打印迭代器中（年、月、日、星期数字）
