import time
from datetime import datetime

dt_01 = datetime.utcnow()
# 内部原理为
timestamp = time.time()  # 获取时间戳
dt_02 = datetime.utcfromtimestamp(timestamp)
print(f"dt_01 = {dt_01}， \ndt_02 = {dt_02}")
