import time

def time2isoz(t=None):
    """
    返回一个"YYYY-MM-DD hh:mm:ssZ"格式的时间字符串，例如：2020-11-11 08:49:37Z
    参数t表示时间戳，如果没有传递参数t,则使用当前时间
    """
    # 判断参数t是否存在，如果不存在则使用当前时间
    if t is None: t = time.time()
    # 获取时间元组的前6个元素
    year, mon, mday, hour, min, sec = time.gmtime(t)[:6]
    # 返回"YYYY-MM-DD hh:mm:ssZ"格式的时间字符串
    return "%04d-%02d-%02d %02d:%02d:%02dZ" % (
        year, mon, mday, hour, min, sec)

if __name__ == "__main__":
    print(time2isoz())
