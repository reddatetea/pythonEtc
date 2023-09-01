from datetime import datetime  # 导入datetime模块中的datetime类
dt = datetime.strptime('28/05/20 14:45', '%d/%m/%y %H:%M')
print(dt)            # 打印日期时间对象
import datetime  # 导入datetime模块
dt = datetime.datetime.strptime('20-5-28', '%y-%m-%d')
print(dt)            # 打印日期时间对象
dt = datetime.datetime.strptime('20-5-28 14:45:20', '%y-%m-%d %H:%M:%S')
print(dt)