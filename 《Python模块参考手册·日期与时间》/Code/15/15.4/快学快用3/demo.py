from calendar import Calendar
from datetime import date

def week_calendar():
    cal = Calendar() # 获取Calendar实例对象
    # 日期增加指定天数
    today = date.today()
    # 获取指定年月的周列表
    weeks = cal.monthdatescalendar(today.year, today.month)
    current_week = []
    # 遍历一年内的周列表
    for week in weeks:
        # 获取本周数据
        if week[0] <= today <= week[6]:
            current_week = week
            break
    # 返回一周数据
    return current_week

if __name__ == "__main__":
    print(week_calendar())