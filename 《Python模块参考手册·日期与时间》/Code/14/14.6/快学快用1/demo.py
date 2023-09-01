from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
print('返回的迭代器为：',calendar_obj.iterweekdays())     # 打印迭代器对象
# 将返回的迭代器转换为列表，其中的值表示星期一至星期日，0为星期一，一周的第一天
print('将迭代器转换为列表：',list(calendar_obj.iterweekdays()))
