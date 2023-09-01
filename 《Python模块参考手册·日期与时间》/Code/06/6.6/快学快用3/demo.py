from datetime import time  # 导入datetime模块中的time类

t = time(16, 13, 56, 888)  # 创建时间对象
print(t.tzinfo)  # 在没有指定时区参数时，返回None
