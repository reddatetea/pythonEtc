import time
import os
import random
import socket

def make_msgid(idstring=None):
    """
    返回一个适合于RFC 2822标准的兼容的Message-ID，例如：
    <20020201195627.33539.96671@nightshade.la.mastaler.com>
    idstring参数是可选项，如果给定，可以增强消息id的唯一性
    """
    timeval = time.time() # 获取时间戳
    # 转化为年月日时分秒的时间格式
    utcdate = time.strftime('%Y%m%d%H%M%S', time.gmtime(timeval))
    # 获取进程id
    pid = os.getpid()
    # 生成一个100000以内的随机整数
    randint = random.randrange(100000)
    # 判断idstring参数是否存在，如果不存在否则为空字符串
    # 如果存在，则使用"."拼接
    if idstring is None:
        idstring = ''
    else:
        idstring = '.' + idstring
    # 返回全称域名
    idhost = socket.getfqdn()
    # 拼接心得字符串
    msgid = '<%s.%s.%s%s@%s>' % (utcdate, pid, randint, idstring, idhost)
    return msgid

if __name__ == "__main__":
    print(make_msgid())
