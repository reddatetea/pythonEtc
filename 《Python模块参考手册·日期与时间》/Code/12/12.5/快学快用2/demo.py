import calendar       # 导入日历模块
month_list = list(calendar.month_name)# 将数组转换为列表
for i in month_list:
    if i!='':                      # 去除空的列表元素
        if month_list.index(i)%2==0:
            print('偶数月：',i)    # 输出偶数月份的英文名称
        else:
            print('奇数月：',i)    # 输出奇数月份的英文名称
