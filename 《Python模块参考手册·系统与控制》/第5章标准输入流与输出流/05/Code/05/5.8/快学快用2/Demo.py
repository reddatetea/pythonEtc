import sys
sys.stdout.write('请输入用户名：')
name=sys.stdin.readline()[:-1]
sys.stdout.write('请输入密码：')
pwd=sys.stdin.readline()[:-1]
if name=='mike' and pwd=='123456':
    print('正在登录程序员之家商务系统！')
else:
    sys.stderr.write('用户名或密码错误，请重新输入！')