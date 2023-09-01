from datetime import  date    # 导入datetime模块中的date类
date_object = date(2019,8,13)   # 创建指定日期的date对象
print(str(date_object)+'为  星期'+str(date_object.isoweekday()))
