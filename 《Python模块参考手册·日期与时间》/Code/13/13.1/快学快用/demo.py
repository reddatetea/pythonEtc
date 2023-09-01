from calendar import Calendar  # 导入日历模块中的Calendar类
c = Calendar()     # 创建默认的Calendar对象
print(list(c.iterweekdays()))       # 返回一周星期几的迭代器
c = Calendar(firstweekday=6)        # 设置周日为一周的第一天
print('设置周日为一周的第一天：')
print(list(c.iterweekdays()))       # 返回一周星期几的迭代器
