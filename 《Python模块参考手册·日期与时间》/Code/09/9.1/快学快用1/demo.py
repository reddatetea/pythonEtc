from datetime import datetime  # 导入datetime模块中的datetime类
from datetime import date      # 导入datetime模块中的date类
from datetime import time      # 导入datetime模块中的time类
d = date(2020,5,21)             # 创建日期对象
t = time(14,11)                 # 创建时间对象
print(datetime.combine(d,t))    # 打印合并后的datetime对象
