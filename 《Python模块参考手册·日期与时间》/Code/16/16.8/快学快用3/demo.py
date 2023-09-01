from calendar import HTMLCalendar      # 导入日历模块中的HTMLCalendar类
from bs4 import BeautifulSoup          # 导入HTML解析模块
htmlcalendar_object = HTMLCalendar()    # 创建HTMLCalendar对象
html = htmlcalendar_object.formatyear(2020)   # 获取指定年份的HTML代码
bs = BeautifulSoup(html,"html.parser")        # 解析HTML
table_all = bs.find_all('table')              # 获取所有的table标签
print(table_all[5])                           # 打印5月份所对应的标签内容