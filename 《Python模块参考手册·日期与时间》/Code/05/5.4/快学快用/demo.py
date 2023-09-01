from datetime import  date    # 导入datetime模块中的date类
date_object = date(2020,5,20)   # 创建指定日期的date对象
print(date_object.__str__())    # 打印返回的日期字符串
print(str(date_object)+'类型为：',type(date_object))
print(date_object.__str__()+'类型为：',type(date_object.__str__()))