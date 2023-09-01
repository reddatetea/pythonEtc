from datetime import  date    # 导入datetime模块中的date类
date_object = date(2020,5,20)   # 创建指定日期的date对象
print(str(date_object)+'类型为：',type(date_object))
print(date_object.isoformat()+'类型为：',type(date_object.isoformat()))