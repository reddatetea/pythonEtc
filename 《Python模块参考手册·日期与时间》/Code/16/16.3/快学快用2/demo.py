import calendar                                  #导入日历模块

data = calendar.calendar(2020,w=2,l=1,c=8,m=6)  #获取2019年日历
# 写入到文本文件
with open('calendar.txt','w') as f:
    f.write(data)