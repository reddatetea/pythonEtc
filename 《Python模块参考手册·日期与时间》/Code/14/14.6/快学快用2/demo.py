from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj2= Calendar(firstweekday=6)       # 创建Calendar对象并指定firstweekday值为6
print('将迭代器转换为列表：',list(calendar_obj2.iterweekdays()))
