import datetime     # 导入日期时间模块
now = datetime.datetime.today()           # 获取当前日期与时间
def is_week(nextday):                     # 根据英文判断星期几
    if nextday.strftime('%A')=='Monday':
        return '（星期一）'
    elif nextday.strftime('%A')=='Tuesday':
        return '（星期二）'
    elif nextday.strftime('%A')=='Wednesday':
        return '（星期三）'
    elif nextday.strftime('%A')=='Thursday':
        return '（星期四）'
    elif nextday.strftime('%A')=='Friday':
        return '（星期五）'
    elif nextday.strftime('%A')=='Saturday':
        return '（星期六）'
    elif nextday.strftime('%A') == 'Sunday':
        return '（星期日）'

def fut(num):
    nextday = now + datetime.timedelta(days=days)   # 计算未来日期与时间
    print('未来',num,'天后是: '  + nextday.strftime('%Y-%m-%d ') +  nextday.strftime('%A')+is_week(nextday))
days = int(input('请输入未来天数，内容必须是数字！:'))      # 获取输入的天数
if days>0:                                                  # 判断输入的数字是否大于0
    fut(days)                                               # 调用计算函数
else:
    print('您输入的内容无法计算未来！')