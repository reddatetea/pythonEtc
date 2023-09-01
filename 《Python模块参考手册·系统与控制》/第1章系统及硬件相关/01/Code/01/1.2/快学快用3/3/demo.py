import os

username = "Python"  # 帐户名
password = "abc"  # 密码
command = "net user %s %s" % (username, password)  # 拼接命令
result = os.system(command)  # 执行命令
if result == 0:  # 如果命令执行成功
    print("修改密码成功，请牢记您的密码！")
else:
    print("修改密码失败！")
