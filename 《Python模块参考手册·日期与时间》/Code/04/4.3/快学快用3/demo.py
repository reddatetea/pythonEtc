import time

while True:
    str = input('输入执行两次函数的时间间隔:')
    if str.isdigit():
        break
n = int(str)  # 休眠的秒数
def func():
    print('%d 秒已经过去了' % n)
while True:
    func()
    time.sleep(n)
