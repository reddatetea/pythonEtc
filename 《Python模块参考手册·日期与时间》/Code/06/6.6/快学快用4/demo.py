import datetime

t1 = datetime.time()  # 创建一个所有参数均为0的时间对象
print('t1：', t1, '，类型为：', type(t1))
t2 = t1.replace(23)  # 将小时替换为23，创建一个新的时间对象
print('t2：', t2, '，类型为：', type(t2))
t3 = t2.replace(minute=30)  # 将分钟替换为30
print('t2：', t3, '，类型为：', type(t3))
