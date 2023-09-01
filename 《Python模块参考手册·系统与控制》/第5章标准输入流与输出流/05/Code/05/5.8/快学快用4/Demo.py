import sys      #  调入系统模块
sys.stdout.write('请输入用户名：')
name=sys.stdin.readline()[:-1]
sys.stdout.write('请输入密码：')
pwd=sys.stdin.readline()[:-1]
if name=='mike' and pwd=='123456':
    print('正在登录程序员之家商务系统！')
else:
    sys.stderr = open('login.txt', 'a+') # 将用户登录错误日志写入文件
    sys.stderr.write('\n'+name+'登录  用户名或密码错误，请重新输入！')