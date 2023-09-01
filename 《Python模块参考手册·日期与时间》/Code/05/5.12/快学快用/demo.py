from datetime import  date    # 导入datetime模块中的date类
date_object = date(2020,5,20)   # 创建指定日期的date对象
print(date_object.strftime('%Y-%m-%d %a %B'))# 打印指定格式的日期字符串