from datetime import date  # 导入datetime模块中的date类
import time  # 导入时间模块

print(date.fromtimestamp(time.time()))  # 打印当前时间戳对应的date对象
