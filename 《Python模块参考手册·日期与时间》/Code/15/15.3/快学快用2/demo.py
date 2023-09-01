from calendar import Calendar

def get_week_wireframe(year, month, day):
    """
    获取当前日期所在一周的日期信息
    :param year: 年
    :param month: 月 
    :param day: 日
    :return: 返回字典类型数据，包括当前一周、年、月、日信息
    """
    # 将年月日转化为整数格式
    year, month, day = int(year), int(month), int(day)
    cal = Calendar() # 获取Calendar实例对象
    # 调用monthdays2calendar方法获取指定月份中日期和天数的二维列表
    monthly_days = cal.monthdays2calendar(year, month)
    current_week = None
    # 遍历日期和天数列表
    for week in monthly_days:
        # 获取当前日期所在的一周数据
        if [i for i, v in enumerate(week) if v[0] == day]:
            current_week = week
    # 返回字典格式数据
    return {"week": current_week, "year": year, "month": MONTHS[month], "today": day}

if __name__  == "__main__":
    MONTHS = [i for i in range(0, 12)] # 1月到12月列表
    print(get_week_wireframe(2020,5,20))