import time                          # 导入time模块
print(time.localtime())             # 获取本地当前时间的时间元组
print(time.localtime(time.time()))  # 以time.time()返回的时间戳为参数获取本地时间的时间元组
