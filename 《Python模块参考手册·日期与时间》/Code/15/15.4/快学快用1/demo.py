from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
# 获取2019年8月份日期天数，该列表为二维列表
days_list= calendar_obj.monthdayscalendar(2019,8)
for i in days_list:               # 循环遍历列表中的日期天数
    print(i)                      # 打印日期天数