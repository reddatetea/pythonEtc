import calendar                            #导入日历模块
print('默认返回：',calendar.firstweekday())             #默认返回0，即星期一
calendar.setfirstweekday(6)               #将星期日设置为一周第一天
print('修改后：',calendar.firstweekday())            #返回6，即星期日
