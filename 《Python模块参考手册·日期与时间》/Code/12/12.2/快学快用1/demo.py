import calendar                          #导入日历模块
week_list = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
week_array = calendar.day_name            # 获取周一至周日英文名称数组
for i,v in enumerate(week_array):        # 遍历周一至周日英文名称
    print(week_list[i],'的英文名称为：',v)
