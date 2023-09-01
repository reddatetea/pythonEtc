import datetime
import time

while True:
    now = datetime.date.today()  # 获取现在的时间
    now_year = now.year  # 获取当前年份
    college_exam_time = datetime.date(now_year, 6, 7)  # 历年高考时间6月7日
    now_days = now.toordinal()  # 现在到0001-01-01的天数
    col_days = college_exam_time.toordinal()  # 高考到0001-01-01的天数
    days = col_days - now_days  # 获取剩余天数

    if days in [-1, 0]:
        end_str = '高考正在进行中！'
    elif days < 0:
        days = datetime.date(now_year + 1, 6, 7).toordinal() - now_days
        end_str = '距离高考还有 %d 天' % days
    else:
        end_str = '距离高考还有 %d 天' % days

        for i in end_str:
            print(i, end='')  # 逐字打印
            time.sleep(0.5)
        print('\r', '', end='')  # 清空控制台
        time.sleep(1)
