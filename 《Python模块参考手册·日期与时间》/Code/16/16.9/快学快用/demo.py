from calendar import HTMLCalendar      # 导入日历模块中的HTMLCalendar类
htmlcalendar_object = HTMLCalendar()    # 创建HTMLCalendar对象
html_bytes = htmlcalendar_object.formatyearpage(2019) # 获取字节类型的HTML页面代码
print(html_bytes.decode(encoding='utf-8')) # 打印2019年日历对应的HTML页面代码