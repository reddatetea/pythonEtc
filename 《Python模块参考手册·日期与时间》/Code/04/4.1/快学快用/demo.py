import time  # 导入time模块
t = (2020,5,20,21,36,54,3,347,0)  # 创建一个名称为t的时间元组
print('指定时间元组：     ',time.asctime(t))              # 指定时间元组
print('默认时间元组：     ',time.asctime())               # 参数为空
print('UTC时区的时间元组：',time.asctime(time.gmtime()))  # 设置参数为time.gmtime()
