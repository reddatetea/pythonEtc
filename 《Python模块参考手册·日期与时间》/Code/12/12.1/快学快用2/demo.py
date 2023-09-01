import calendar  # 导入日历模块
# 根据星期几返回数字0至6
def myweek(name):
    week_dict = {
        '星期一': 0,
        '星期二': 1,
        '星期三': 2,
        '星期四': 3,
        '星期五': 4,
        '星期六': 5,
        '星期日': 6
    }
    return week_dict[name]
week = input('请输入星期：')  # 输入星期
week_array = calendar.day_abbr  # 获取周一至周日英文缩写数组
for i, v in enumerate(week_array):  # 遍历周一至周日英文缩写
    if i == myweek(week):  # 调用自定义函数将输入的星期转换为数字并进行判断
        print(week, '的英文缩写为：', v)
