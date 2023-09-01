from calendar import Calendar     # 导入日历模块中的Calendar类

def get_feb_days(year):
    calendar_obj = Calendar()          # 创建默认的Calendar对象
    # 获取日期和天数的二维列表
    days_list= calendar_obj.monthdayscalendar(year,2)
    return max(days_list[-1])

if __name__ == "__main__":
    year = int(input('请输入年份:'))
    days = get_feb_days(year)
    print(f'{year}年2月份共有{days}天')