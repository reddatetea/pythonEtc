import datetime
import time
dt = datetime.datetime(2020, 5, 20)  # 获取datetime对象
print(dt)
timetuple = dt.timetuple()  # 转换为时间元组
print('时间元组为：', timetuple)
epoch = time.mktime(timetuple)  # 将时间元组转换为时间戳
print(epoch)
