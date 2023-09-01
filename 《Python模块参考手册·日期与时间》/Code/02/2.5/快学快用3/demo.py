import time                 # 导入time模块
t = time.localtime()         # localtime()方法获取本地当前时间的时间元组
print('本地当前时间的时间元组为：',t)          # 输出本地当前时间的时间元组
print('属性名获取的年份为：',t.tm_year, "年")  # 通过“.属性名”的方式获取年份
print('下标索引获取的月份为：',t[1], "月")     # 通过下标索引获取月份
