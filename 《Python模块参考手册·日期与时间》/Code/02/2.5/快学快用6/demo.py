import time

def Time2Internaldate(date_time):
    """
    将日期时间转化为IMAP4 INTERNALDATE格式
    返回一个字符串格式为:"DD-Mmm-YYYY HH:MM:SS +HHMM"
    data_time参数可以是整型或浮点型或者是时间元组或者时间字符串
    """
    # 判断是否为整型和浮点型
    if isinstance(date_time, (int, float)):
        tt = time.localtime(date_time)
    # 判断是否为时间结构元组
    elif isinstance(date_time, (tuple, time.struct_time)):
        tt = date_time
    # 判断是否为字符串类型
    elif isinstance(date_time, str) and (date_time[0], date_time[-1]) == ('"', '"'):
        return date_time  # Assume in correct format
    else:
        raise ValueError("date_time not of a known type")
    # 组织时间格式
    dt = time.strftime("%d-%b-%Y %H:%M:%S", tt)
    if dt[0] == '0':
        dt = ' ' + dt[1:]
    if time.daylight and tt[-1]:
        zone = -time.altzone
    else:
        zone = -time.timezone
    return '"' + dt + " %+03d%02d" % divmod(zone//60, 60) + '"'

if __name__ == "__main__":
    # 将时间戳转化为IMAP4 INTERNALDATE格式
    print(Time2Internaldate(time.time()))
    # 将时间元组转化为IMAP4 INTERNALDATE格式
    print(Time2Internaldate(time.gmtime()))
    # 普通字符串直接返回
    print(Time2Internaldate('"20-May-2020"'))
