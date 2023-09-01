import datetime
import time

def default(obj):
    # 如果obj是日期时间格式，则调用utctimetuple()方法
    if isinstance(obj, datetime.datetime):
        return time.mktime(obj.utctimetuple())
    # 如果obj是日期格式，则调用timetuple()方法
    elif isinstance(obj, datetime.date):
        return time.mktime(obj.timetuple())
    else:
        return None

if __name__ == "__main__":
    # 日期时间格式转化为时间戳
    print(default(datetime.datetime(2020,5,20)))
    # 日期格式转化为时间戳
    print(default(datetime.date(2020,5,20)))
