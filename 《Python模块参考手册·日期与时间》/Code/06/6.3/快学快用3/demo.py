import datetime

t1 = datetime.time()  # 创建一个将时间属性为0的时间对象
print('替换前的t1:', t1)
tt = (21, 30, 45, 99999)  # 创建实例化时间对象所需的元组
t2 = t1.replace(*tt)  # 使用元组替换时间对象的属性，记得加*号
print('替换后的t1:', t1)  # 查看是否改变了原属性
print('t2        :', t2)
