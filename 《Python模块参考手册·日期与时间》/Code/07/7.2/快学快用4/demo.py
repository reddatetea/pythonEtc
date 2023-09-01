import datetime

ddt = datetime.datetime.today()  # 获取今天的日期时间对象
print('ddt：', ddt, '，ddt的类型为：', type(ddt))
year = ddt.year  # 获取年
month = ddt.month  # 获取月
day = ddt.day  # 获取日
da = datetime.date(year, month, day)  # 生成日期对象
print('da ：', da, '，da 的类型为：', type(da))
