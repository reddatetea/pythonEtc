import calendar                       #导入日历模块
# 循环检测2010年至2020年是平年还是闰年
for i in range(2010,2021,1):
    n=calendar.leapdays(i,i+1)   #检测每一年的闰年个数
    # 大于零为闰年，否则为平年
    if n>0:
        print(i,'年：闰年')
    else:
        print(i, '年：平年')
