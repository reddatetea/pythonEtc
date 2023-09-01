from datetime import time  # 导入datetime模块中的time类

t = time(16, 13, 56, 888)  # 创建时间对象
new_time = t.replace(16, 28, 40, 567)  # 替换时间对象
print('原对象：', t)
print('新对象：', new_time)
