from datetime import date  # 导入datetime模块中的date类

date_object = date(2019, 5, 1)  # 创建指定日期的date对象
print('原对象：', date_object)  # 打印原date对象
print('新对象：', date_object.replace(2020, 8, 13))  # 打印替换后的新date对象
print('原对象id为：', id(date_object))
print('新对象id为：', id(date_object.replace(2020, 8, 13)))
