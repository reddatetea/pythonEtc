from datetime import datetime  # 导入datetime模块中的datetime类
dt = datetime.now()             # 获取当前的日期时间对象
str_dt = dt.isoformat()         # 获取日期时间字符串
# 打印根据指定的日期时间字符串返回对应的datetime对象
print(datetime.fromisoformat(str_dt))