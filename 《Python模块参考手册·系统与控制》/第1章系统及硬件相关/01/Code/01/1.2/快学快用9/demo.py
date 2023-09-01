import os
name = "以太网"  # 适配器名称
primary_dns = "223.5.5.5"  # 主DNS
secondary_dns = "223.6.6.6"  # 副DNS
# 设置主DNS的命令
command1 = 'netsh interface ip set dns "%s" source=static addr=%s' % (name, primary_dns)
# 设置副DNS的命令
command2 = 'netsh interface ip add dns "%s" %s index=2' % (name, secondary_dns)
os.system(command1)  # 执行命令
os.system(command2)
print("修改DNS完毕")
