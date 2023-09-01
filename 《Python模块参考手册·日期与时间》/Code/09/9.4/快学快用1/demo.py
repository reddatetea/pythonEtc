from datetime import datetime  # 导入datetime模块中的datetime类
from datetime import date      # 导入datetime模块中的date类
days = date.today().toordinal()   # 获取自0001年01月01日开始的第多少天
print(datetime.fromordinal(days)) # 打印公历序数对应的datetime对象
