from calendar import TextCalendar      # 导入日历模块中TextCalendar类
year = input('请输入需要查询的年份！')  # 如，2020
if year.isdigit():
    textcalendar_object = TextCalendar()    # 创建TextCalendar对象
    # 获取指定年中所有月份的字符类型日历
    textcalendar=textcalendar_object.formatyear(int(year),m=6)
    file = open('textcalendar.txt','w')                    # 写入模式
    file.write(textcalendar)                               # 将日历字符串写入文件
    file.close()                                           # 关闭