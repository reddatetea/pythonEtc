import os
date = "2020/01/01"  # 指定日期
command = "date " + date  # 拼接命令
reslut = os.system(command)  # 执行命令
if reslut == 0:  # 如果命令成功执行
    print("修改成功")
else:
    print("修改失败")
