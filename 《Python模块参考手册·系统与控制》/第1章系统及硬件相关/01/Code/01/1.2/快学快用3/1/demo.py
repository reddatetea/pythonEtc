import os
username = "Python"  # 帐户名
password = "123456"  # 密码
command = "net user %s %s /add" % (username, password)  # 拼接命令
result = os.system(command)  # 执行命令
if result == 0:  # 如果命令执行成功
    print("创建新帐户成功")
else:
    print("创建失败！")
