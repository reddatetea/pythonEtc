import os
value = os.getenv("mr")  # 尝试获取名为mr环境变量
if value is None:  # 如果没有这个环境变量
    print("系统不存在%s环境变量" % value)
else:
    print("mr = " + value)
