import os

username = "Python"  # 帐户名
command = "net localgroup administrators %s /add" % username  # 拼接命令
result = os.system(command)  # 执行命令
if result == 0:  # 如果命令执行成功
    print(username + "已转为管理员")
else:
    print("更改帐户类型失败")
