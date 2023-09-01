from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
# 获取2019年每个月的日期天数与星期数字，该列表为四维列表
dates_week_list= calendar_obj.yeardays2calendar(2019,1)
for i in dates_week_list:         # 循环遍历列表中的日期天数与星期数字
    print(i)                      # 打印一年中每月的日期天数与星期数字的列表