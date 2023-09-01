import sys
import time
from datetime import datetime, date

# 五种不同的方式获取时间戳
stamp01 = datetime(2020, 12, 23).timestamp()
stamp02 = time.mktime(time.localtime())
stamp03 = time.mktime(time.gmtime())
stamp04 = time.mktime(datetime(2020, 10, 10).timetuple())
stamp05 = time.mktime(date(2018, 8, 10).timetuple())
# 根据时间戳 创建 UTC 时间的 datetime 对象
for index in range(1, 6):
    if hasattr(sys.modules[__name__], "stamp0" + str(index)):
        var = getattr(sys.modules[__name__], "stamp0" + str(index))
        obj = datetime.utcfromtimestamp(var)
        print(f"stamp0{str(index)} -----> UTCDatetime :{obj}")
