import sys
print('请输入数字验证码：')
numbers = sys.stdin.readline().strip('\n') # 输入验证码
# 如果验证码均为数字且验证码为123456
if numbers.isdigit() and numbers == 123456:
    print('正在登录程序员之家商务系统！')
else:
    print('输入了非数字字符，请重新输入！')