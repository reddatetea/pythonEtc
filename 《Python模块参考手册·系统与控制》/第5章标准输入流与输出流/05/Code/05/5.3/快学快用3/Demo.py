import sys
print('请输入6位数字密码:') # 提示用户输入字符串
password = sys.stdin.readline().strip('\n') # 去除6位数字密码末尾处的换行符“\n”
if (password == '624351'):
    print('密码正确！')
else:
    print('密码错误！请重新输入……')