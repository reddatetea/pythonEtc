from datetime import datetime  # 导入datetime模块中的datetime类
dt = datetime.today()    # 获取当前日期时间
new_dt = dt.replace(2020,12,25,22,15,38,888)  # 替换原对象获取新对象
print('原对象：',dt)
print('新对象：',new_dt)
print('原对象id为：',id(dt))
print('新对象id为：',id(new_dt))
