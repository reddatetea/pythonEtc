import os

key_name = "mrsoft"  # 要添加的项名称
command = 'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\%s"' % key_name # 拼接命令
result = os.system(command)  # 执行添加命令
if result == 0:  # 如果命令执行成功
    print("添加注册表成功")
else:
    print("无法添加注册表！")
