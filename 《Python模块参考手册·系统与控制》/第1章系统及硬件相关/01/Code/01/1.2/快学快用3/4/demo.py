import os

username = "Python"  # 帐户名
command = "net user %s /delete" % username  # 拼接命令
result = os.system(command)  # 执行命令
if result == 0:  # 如果命令执行成功
    print("帐户" + username + "已删除！")
else:
    print("删除帐户失败")
