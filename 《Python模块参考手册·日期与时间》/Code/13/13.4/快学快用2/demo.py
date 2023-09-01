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
# 输出2020年每个月的天数以及第一天是星期几
for i in range(1, 13):
    mytuple = calendar.monthrange(2020, i)  # 获取2020年
    print('2020年', str(i), '月')
    print(mytuple[1], '天 第一天是：', myweek(mytuple[0]))
