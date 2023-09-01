import time
import datetime
t = time.ctime()
print(t)
f = datetime.datetime.strptime(t, '%a %b %d %H:%M:%S %Y')  # 格式化为指定格式
print(f)
