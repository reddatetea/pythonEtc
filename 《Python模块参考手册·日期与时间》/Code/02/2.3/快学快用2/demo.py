import time  # 导入time模块
millis = time.time() * 1000   # 获取时间戳毫秒数
millis_int = int(round(time.time() * 1000))  # 四舍五入并取整
print('时间戳的毫秒为：',millis)
print('四舍五入取整后：',millis_int)
