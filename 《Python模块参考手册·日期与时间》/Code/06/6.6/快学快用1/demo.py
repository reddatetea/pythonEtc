from datetime import time  # 导入datetime模块中的time类

t = time(16, 13, 56, 888)  # 创建时间对象
print(t)
print(t.hour, t.minute, t.second, t.microsecond)  # 获取时、分、秒、微秒
