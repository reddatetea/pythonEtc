from calendar import HTMLCalendar      # 导入日历模块中的HTMLCalendar类
htmlcalendar_object = HTMLCalendar(firstweekday=6) # 创建一周第一天为星期日的HTMLCalendar对象
# 打印2020年5月日历HTML表格代码，该日历一周的第一天为星期日
print(htmlcalendar_object.formatmonth(2020,5))