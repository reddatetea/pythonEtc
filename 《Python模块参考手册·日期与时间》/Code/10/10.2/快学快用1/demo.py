from datetime import timedelta   # 导入datetime模块中的timedelta类
td = timedelta(365,888,687411)    # 创建timedelta对象
print(td.total_seconds())    # 时间差中包含的总秒数
