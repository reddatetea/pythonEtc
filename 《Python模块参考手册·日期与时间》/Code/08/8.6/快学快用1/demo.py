from datetime import date  # 导入datetime模块中的date类

# 星期列表
week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', ]
date_object = date(2019, 8, 13)  # 创建指定日期的date对象
week_code = date_object.weekday()  # 获取指定日期对应的星期码
print(date_object, '为', week_list[week_code])  # 打印指定日期为星期几
