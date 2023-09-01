from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
year=int(input('请输入年份：'))    # 年份
month=int(input('请输入月份：'))   # 月份
mydate=calendar_obj.itermonthdates(year,month)  # 获取日期迭代器
for i in mydate:               # 循环遍历迭代器中的日期
    if i.month==month:         # 判断是否为输入的月份
        print(i)               # 输出迭代器中的日期
