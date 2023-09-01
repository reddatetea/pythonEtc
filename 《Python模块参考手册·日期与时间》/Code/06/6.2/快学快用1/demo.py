from datetime import time  # 导入datetime模块中的time类

t = time(16, 13, 56, 888)  # 创建时间对象
time_str = t.isoformat()  # 获取时间字符串
print(time_str, '对应的类型为：', type(time_str))
time_object = time.fromisoformat(time_str)  # 获取时间字符串对应的时间对象
print(time_object, '对应类型为：', type(time_object))
