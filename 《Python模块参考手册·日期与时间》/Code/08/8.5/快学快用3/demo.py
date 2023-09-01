from datetime import date, timedelta, datetime

y = 2020  # 定义年份
m = 5  # 定义月份
w = 3  # 定义星期几

all_days = (date(y, m + 1, 1) - date(y, m, 1)).days  # 当前月份共有多少天
day_start = date(y, m, 1)  # 月份初始日期
day_last = date(y, m, all_days)  # 月份结束日期
delta = day_last - day_start  # 日期差
data_list = []
for i in range(delta.days + 1):
    p = (day_start + timedelta(days=i)).strftime('%Y-%m-%d')  # 具体哪一天
    pp = datetime.strptime(str(p), '%Y-%m-%d')  # 转为datetime类型
    wd = pp.weekday()
    if wd == w - 1:  # 判断星期几
        d2 = pp.strftime('%Y-%m-%d')
        data_list.append(d2)

print('%d年%d月中共有%d个星期%d' % (y, m, len(data_list), w))
print('具体日期分别为：', data_list)
