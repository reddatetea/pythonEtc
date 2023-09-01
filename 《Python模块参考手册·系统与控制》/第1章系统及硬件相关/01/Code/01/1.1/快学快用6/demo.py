import os
url = "www.baidu.com"  # 测试的连接
print("正在尝试连接 " + url + " ...")
command = "ping " + url + " -n 1" # 拼接命令
proxy = os.popen(command)  # 执行一次ping命令
result = str(proxy.read())  # 读取文件流中的内容
if "Ping 请求找不到主机" in result:
    print("网络故障，请检查网络设备和DNS参数")
elif "丢失 = 0" in result:
    print("哇塞，你的网络畅通无阻！")
elif "丢失 = 1" in result:
    print("你的网络不太稳定哦，是不是该重启路由器了？")
else:
    print("不支持此操作系统")
