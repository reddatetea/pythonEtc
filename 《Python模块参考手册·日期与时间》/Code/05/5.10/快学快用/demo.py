from datetime import time     # 导入datetime模块中的time类
t=time(16,13,56,888)    #创建时间对象
print(t.isoformat())        # 打印默认格式的时间字符串
print(t.isoformat('hours'))
print(t.isoformat('minutes'))
print(t.isoformat('seconds'))
print(t.isoformat('milliseconds'))
print(t.isoformat('microseconds'))