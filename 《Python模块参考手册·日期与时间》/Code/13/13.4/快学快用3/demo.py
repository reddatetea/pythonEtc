import calendar                   # 导入日历模块
n=0                               # 初始值
#循环输出5月至8月并计算每个月的天数
for i in range(5,8,1):
    mytuple=calendar.monthrange(2020,i)
    print(i,'月',mytuple[1],'天')
    n=n+mytuple[1]     # 累计求和
print('总计：',n,'天') # 输出总计天数
