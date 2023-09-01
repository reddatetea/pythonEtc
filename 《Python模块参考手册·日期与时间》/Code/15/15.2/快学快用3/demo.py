from calendar import Calendar
from datetime import datetime,timedelta

def m_to_expiry(m_expiry):
    c = Calendar() # 获取Calendar实例化对象
    # 将字符串转化为日期格式
    expiry = datetime.strptime(m_expiry, '%Y%m%d')
    # 获取月份中的日期天数
    mdc = c.monthdatescalendar(expiry.year, expiry.month)
    # 获取本月的所有周五的日期
    sunday = [x[6] for x in mdc if x[6].month == expiry.month]
    # 如果输入日期为周日，则推迟1天
    if expiry.date() in sunday:
        expiry += timedelta(days=1)
    # 返回推迟后的日期
    return expiry.strftime('%Y-%m-%d')

if __name__ == "__main__":
    date  = input('请输入截止日期,例如20200520:')
    expiry_date = m_to_expiry(date)
    print(f'截止日期为{expiry_date}')