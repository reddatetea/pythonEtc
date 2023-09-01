from datetime import date  # 导入datetime模块中的date类

date_object = date(2019, 5, 12)  # 创建指定日期的date对象
print(date_object.toordinal())  # 打印自0001年01月01日开始至当前日期对象的天数
