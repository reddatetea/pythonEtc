from datetime import datetime  # 导入datetime模块中的datetime类
dt=datetime.today()         #把获取的当前本地日期时间赋给变量dt
print(dt.astimezone())          # 打印带有时区信息的datetime对象
