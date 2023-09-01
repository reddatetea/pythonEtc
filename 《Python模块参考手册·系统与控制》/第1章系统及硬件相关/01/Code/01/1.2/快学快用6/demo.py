import os
time = "00:15:00"  # 指定时间
command = "time " + time  # 拼接命令
reslut = os.system(command)  # 执行命令
if reslut == 0:  # 如果命令成功执行
    print("修改成功")
else:
    print("修改失败")
