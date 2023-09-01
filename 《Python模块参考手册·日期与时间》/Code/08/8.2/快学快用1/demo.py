from datetime import datetime  # 导入datetime模块中的datetime类

dt = datetime.today()  # 获取当前日期时间
print(dt.isocalendar())  # 打印当前日期的年份、周数、星期数的元组
