import calendar

def getLaborDay(year):
    month = 9
    # 获取Calendar实例化对象
    mycal = calendar.Calendar()
    # 调用monthdatescalendar方法，获取指定月份的日期列表
    cal = mycal.monthdatescalendar(year, month)
    # 判断第1个星期一是否在本月，如果是，则获取第1个列表的第1个元素
    # 否则，获取第2个列表的第1个元素
    if cal[0][0].month == month:
        return cal[0][0]
    else:
        return cal[1][0]

print(getLaborDay(2020))