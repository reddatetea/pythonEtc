import random                # 导入随机模块
import calendar              # 导入日历模块
list=[0,1,2,3,4,5,6]         # 0-6的数字列表
day_randoms=random.sample(list,3)  # 随机不重复（从列表中随机抽取3个数字）
print('随机抽取的数字是：',day_randoms)
#将随机抽取的数字转换为与之对应的星期的英文名称
print('对应的星期如下：')
week_array = calendar.day_name            # 获取周一至周日英文名称数组
for i in day_randoms:
    print(week_array[i])
