import os

def back_up_reg2(reg, file_path):
    command = 'reg export "%s" %s /y' % (reg, file_path)  # 拼接命令
    result = os.system(command)  # 执行命令
    return result == 0  # 如果命令执行成功

# 备份的注册表项
reg = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer"
file = "D:\\test\\backup.reg"  # 备份文件的地址
result = back_up_reg2(reg, file)

if result:
    print("备份完毕")
else:
    print("备份失败")
