from datetime import datetime  # 导入datetime模块中的datetime类

dt = datetime.today()  # 获取当前日期时间
print(dt)  # 打印日期时间
print(dt.date())  # 打印日期时间对象中的日期部分
print(type(dt))  # 打印日期时间的类型
print(type(dt.date()))  # 打印日期部分的类型
