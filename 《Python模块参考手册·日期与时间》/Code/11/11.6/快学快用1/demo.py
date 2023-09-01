from datetime import datetime  # 导入datetime模块中的datetime类
dt=datetime.today()         #把获取的当前本地日期时间赋给变量dt
print(dt.timetz())          # 打印日期时间对象对应的时区时间
