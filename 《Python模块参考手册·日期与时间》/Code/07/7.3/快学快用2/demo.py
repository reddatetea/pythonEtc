import datetime

date_str = '2020-10-10'  # 日期字符串
print('date_str:', date_str, 'type:', type(date_str))
date_format = datetime.date.fromisoformat(date_str)  # 转换为日期对象
print('date_format:', date_format, 'type:', type(date_format))
