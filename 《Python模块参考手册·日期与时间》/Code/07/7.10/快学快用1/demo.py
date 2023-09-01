from datetime import datetime  # 导入datetime模块中的datetime类

dt = datetime.today()  # 获取当前日期时间
print(dt.toordinal())  # 打印自0001年01月01日开始至当前日期时间的天数
