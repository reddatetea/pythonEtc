import calendar

year = int(input('请输入年份，如2020:'))
month = calendar.monthcalendar(year, 11)
# 判断第1周是否有周四
if month[0][3]:       # 如果第1周有周四，从第1周开始计算
    day = month[3][3]
else:                 # 如果第1周没有周四，从第2周开始计算
    day = month[4][3]
# 输出感恩节日期
date = f'{year}-11-{day}'
print(f'{year}年的感恩节是{date}')