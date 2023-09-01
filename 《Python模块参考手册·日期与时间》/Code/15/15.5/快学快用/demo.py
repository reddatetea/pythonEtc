from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
# 获取2019年每个月所有日期，该列表为四维列表
dates_list= calendar_obj.yeardatescalendar(2019,1)
for i in dates_list:               # 循环遍历列表中的日期
    print(i)                      # 打印一年中每月的日期列表