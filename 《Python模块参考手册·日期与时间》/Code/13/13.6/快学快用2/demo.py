import calendar  # 导入日历模块
# 根据数字0至6返回星期几
def myweek(n):
    week_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日'
    }
    return week_dict[n]
# 输入日期
date = input('请输入日期(格式为：dddd,m,d)：')
# 将日期分割为列表
date_list = list(map(int, date.split(',')))
# 获取日期的星期码
n = calendar.weekday(date_list[0], date_list[1], date_list[2])
# 星期码转换为星期几的格式后输出
print('今天是：', myweek(n))
