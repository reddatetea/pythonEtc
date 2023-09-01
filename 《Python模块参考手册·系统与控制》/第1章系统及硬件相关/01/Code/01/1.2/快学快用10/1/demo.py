import os

def back_up_reg(reg, file_path):
    command = 'regedit /e %s "%s"' % (file_path, reg)  # 拼接命令
    result = os.system(command)  # 执行命令
    return result == 0  # 如果命令执行成功

# IE浏览器的注册表项
reg = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer"
file = "D:\\test\\backup.reg"  # 备份文件的完整名称
result = back_up_reg(reg, file)

if result:
    print("备份完毕")
else:
    print("备份失败")
