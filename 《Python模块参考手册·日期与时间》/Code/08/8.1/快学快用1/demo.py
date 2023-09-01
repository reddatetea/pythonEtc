from datetime import date  # 导入datetime模块中的date类

date_object = date(2020, 8, 13)  # 创建指定日期的date对象
date_tuple = date_object.isocalendar()  # 日期对应的年份、周数以及星期数元组
print(str(date_tuple[0]) + '年')
print('第' + str(date_tuple[1]) + '周')
print('星期' + str(date_tuple[2]))
