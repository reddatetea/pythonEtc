import calendar     # 导入日历模块
week_list = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日',]  # 星期列表
week_index=calendar.firstweekday()  # 返回当前周的起始日期（星期几）
print('本周的第一天为：',week_list[week_index])
