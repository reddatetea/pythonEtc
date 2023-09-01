from datetime import datetime  # 导入datetime模块中的datetime类
import time  # 导入时间模块

print(datetime.fromtimestamp(time.time()))  # 根据当前时间戳创建datetime对象
