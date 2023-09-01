from datetime import datetime  # 导入datetime模块中的datetime类
dt = datetime.today()    # 获取当前日期时间
print(dt.__format__('%Y-%m-%d'))    # 打印指定格式的日期字符串