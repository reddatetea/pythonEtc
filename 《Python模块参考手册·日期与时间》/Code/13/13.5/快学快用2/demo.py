import calendar   # 导入日历模块
# 输入年份和月份
year = int(input("输入年份: "))
month = int(input("输入月份: "))
calendar.setfirstweekday(firstweekday=5) #设置第一天是星期六
# 显示日历
print(calendar.month(year,month))
