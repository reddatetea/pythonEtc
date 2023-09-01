from calendar import HTMLCalendar      # 导入日历模块中的HTMLCalendar类
year = input('请输入指定年份！')        # 获取输入的年份
htmlcalendar_object = HTMLCalendar()    # 创建HTMLCalendar对象
calendar_html = htmlcalendar_object.formatyear(int(year))  # 获取指定年份的HTML代码
html = open(year+'年'+'.html','w')                           # 写入模式
html.write(calendar_html)                                  # 写入
html.close()                                               # 关闭