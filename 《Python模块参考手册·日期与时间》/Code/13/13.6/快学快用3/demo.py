import calendar                    # 导入日历模块
from calendar import Calendar      # 导入日历模块中的Calendar类
Mon=[]                             # 创建列表
calendar_obj = Calendar()          # 创建默认的Calendar对象
itermonth= calendar_obj.itermonthdates(2020,8)  # 获取2020年8月的日期迭代器
# 循环遍历迭代器中的日期（其中包含当前月份开始那周与结束那周的所有日期）
for date in itermonth:
    # 日期转换为列表
    date_list = list(map(int,str(date).split('-')))
    # 获取指定日期的星期码
    n=calendar.weekday(date_list[0],date_list[1],date_list[2])
    # 将星期一添加到列表中
    if n==0:
        Mon.append(str(date))
print(Mon)
