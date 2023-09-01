from datetime import datetime  # 导入datetime模块中的datetime类

dt = datetime.today()  # 获取当前日期时间
print(dt)  # 打印日期时间
print(dt.time())  # 打印日期时间对象中的时间部分
print(type(dt))  # 打印日期时间的类型
print(type(dt.time()))  # 打印时间部分的类型
