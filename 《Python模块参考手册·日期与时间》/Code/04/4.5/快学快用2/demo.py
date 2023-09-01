import time
from datetime import datetime

str_t = '30/03/20 16:31:32'
struct_t = time.strptime(str_t, '%d/%m/%y %H:%M:%S')
print('不带毫秒的时间元组 ：', struct_t)

str_s = '30/03/20 16:31:32.123'
struct_s = datetime.strptime(str_s, '%d/%m/%y %H:%M:%S.%f')  # 解析毫秒
print(struct_s)
tt = struct_s.timetuple()  # 转换为时间元组
print('带毫秒的时间元组   ：', tt)
