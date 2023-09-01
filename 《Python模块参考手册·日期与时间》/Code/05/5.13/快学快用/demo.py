from datetime import time     # 导入datetime模块中的time类
t=time(16,13,56,888)    #创建时间对象
print(t.strftime('%H'))      # 打印小时
print(t.strftime('%H:%M'))   # 打印小时与分钟