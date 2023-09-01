import datetime       # 导入日期时间模块
import time           # 导入时间模块
#创建国庆节时间
future = datetime.datetime.strptime('2020-10-1 00:00:00','%Y-%m-%d %H:%M:%S')
today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')    # 获取当前年、月、日
print('今天是'+today)
while True:
    today = datetime.datetime.today()    #获取今天时间
    delta = future - today               # 计算时间差
    hour = int(delta.seconds / 60 / 60)    # 设定的时间距离当前时间的小时差
    minute = int((delta.seconds - hour * 60 * 60) / 60)    # 设定的时间距离当前时间的分钟差
    second = delta.seconds - hour * 60 * 60 - minute * 60  # 设定的时间距离当前时间的秒钟差
    print('\r'+'距离国庆节还有：',str(delta.days)+'天'+str(hour) + '小时' + str(minute) + '分' + str(second) + '秒', end='')
    time.sleep(1)                          # 等待1秒
    if delta.seconds==0:                   # 如果没有时间差，说明已经到10月1日国庆节了
        print('\n国庆节快乐！')
        break