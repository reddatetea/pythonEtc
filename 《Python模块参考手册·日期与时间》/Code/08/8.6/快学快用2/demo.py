import datetime

start_date = datetime.date(2020, 5, 10)  # 开始日期
end_date = datetime.date(2020, 5, 30)  # 结束日期
days = (end_date - start_date).days  # 日期相差的天数
day_list = []  # 空列表，存储数据

for i in range(days + 1):
    one_day = start_date + datetime.timedelta(days=i)  # 开始日期后的第i天
    if one_day.weekday() > 4:  # 判断是否为周末
        day_string = one_day.strftime('%Y-%m-%d')  # 格式化为字符串
        day_list.append(day_string)  # 添加到列表中

print("在这个时间段中，周末共有 {} 天".format(len(day_list)))
print("分别为:", day_list)
