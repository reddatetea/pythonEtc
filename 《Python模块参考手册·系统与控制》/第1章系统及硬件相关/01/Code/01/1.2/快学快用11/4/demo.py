import os

key_name = "mrsoft"  # 要添加的项名称
value_name = "Home Page"  # 要添加的值名称

command = 'reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\%s" /v "%s" /f' % (key_name, value_name)  # 拼接命令
result = os.system(command)  # 执行添加命令
if result == 0:  # 如果命令执行成功
    print("删除注册表值成功")
else:
    print("无法操作注册表！")
