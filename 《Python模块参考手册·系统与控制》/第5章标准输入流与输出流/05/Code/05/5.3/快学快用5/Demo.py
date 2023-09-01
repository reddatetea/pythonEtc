import sys
print('请输入您的密码：')
password = sys.stdin.readline().upper().strip('\n')
print('请输入您的姓名：')
name = sys.stdin.readline().capitalize().strip('\n')
print('请输入您的学校：')
school = sys.stdin.readline().title().strip('\n')
print(password, name, school)