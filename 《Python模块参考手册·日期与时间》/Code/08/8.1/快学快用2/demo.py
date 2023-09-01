import datetime

# 母亲节为每年5月第二个星期天
while True:
    date_str = input('请输入日期字符串，格式为YYYY-MM-DD（例：2020-05-10）：')

    try:
        date_day = datetime.date.fromisoformat(date_str)  # 日期字符串转换为日期格式
    except ValueError as e:
        print('请输入正确的日期格式')
        continue

    # 如果不是5月或者日期不在7号到14号之间 就都不是母亲节
    if date_day.month != 5 or date_day.day not in range(7, 14):
        print('%s 这一天不是母亲节' % date_str)
        continue

    date_iso = date_day.isocalendar()  # 获取年份、周数、星期数的元组

    if date_iso[2] == 7:
        print('%s 这一天是母亲节' % date_str)
    else:
        print('%s 这一天不是母亲节' % date_str)
