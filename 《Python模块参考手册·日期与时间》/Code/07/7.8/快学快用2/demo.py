import datetime

today = datetime.date.today()
print('现在是：', today)
input('请手动改变系统的时间后，在本窗口按下回车！')
today_change = datetime.date.today()
print('现在是：', today_change)
