import os

def update_reg(key_name, value_name, data):
    command = 'reg add "%s" /v "%s" /t REG_SZ /d "%s" /f' % (key_name, value_name, data)# 拼接命令
    result = os.system(command)  # 执行添加命令，会覆盖原有值
    return result == 0  # 如果命令执行成功

key_name = "HKEY_LOCAL_MACHINE\\SOFTWARE\\mrsoft"  # 项名称
value_name = "Home Page"  # 值名称
data = "www.baidu.com"  # 要改的值

if update_reg(key_name, value_name, data):  # 修改注册表
    print("修改注册表成功")
else:
    print("无法操作注册表！")
