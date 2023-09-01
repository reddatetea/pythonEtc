from calendar import TextCalendar      # 导入日历模块中TextCalendar类
year = input('请输入需要查询的年份！')  # 如，2020
month = input('请输入需要查询的月份！') # 如，5
if year.isdigit()and month.isdigit():   # 判断是否为数字
    if int(month)>0and int(month)<13:
        textcalendar_object = TextCalendar()  # 创建TextCalendar对象
        textcalendar_object.prmonth(int(year), int(month))  # 打印指定年指定月份的日历
    else:
        print('您输入的月份应该大于0小于13！')
else:
    print('请输入数字！')