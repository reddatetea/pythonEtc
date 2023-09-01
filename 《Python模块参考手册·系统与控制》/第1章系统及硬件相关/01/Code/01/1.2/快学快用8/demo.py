import os

def modify_ip(name, ip, mask, gateway):  # 设置静态IP地址
    # 拼接命令
    command = 'netsh interface ip set address "%s" static %s %s %s' % (name, ip, mask, gateway)
    result = os.system(command)  # 执行命令
    return result == 0  # 如果命令执行成功

name = "以太网"  # 网卡名称，win10默认叫以太网，win7默认叫本地连接
ip = "192.168.0.10"  # 修改之后的IP
mask = "255.255.255.0"  # 子网掩码
gateway = "192.168.0.1"  # 默认网关
result = modify_ip(name, ip, mask, gateway)
if result:
    print("IP地址修改成功")
else:
    print("无法修改IP地址")
