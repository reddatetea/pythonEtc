import datetime

# 生成两个日期对象
date_0 = datetime.date(2019, 1, 1)
date_1 = datetime.date(2020, 2, 2)
print("date_0: {}".format(date_0))
print("date_1: {}".format(date_1))
date_2 = date_0.replace(year=2019, month=7, day=4)  # 具体日期替换date_0内的数据
print("date_2: {}".format(date_2))
date_3 = date_0.replace(date_1.year, date_1.month, date_1.day)  # 使用date_1替换date_0
print("date_3: {}".format(date_3))
