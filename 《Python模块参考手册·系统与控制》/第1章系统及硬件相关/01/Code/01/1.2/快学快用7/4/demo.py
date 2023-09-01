import os

def shut_down(time):
    command = 'schtasks /create /tn "定时关机" /sc once /tr "shutdown -s " /f /st ' + time
    result = os.system(command)  # 执行命令
    return result == 0  # 如果命令执行成功

time = "20:00:00"
if shut_down(time):
    print("定时关机任务制定完毕")
else:
    print("无法制定定时关机任务")
