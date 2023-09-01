import os

# IE浏览器所在注册表位置
reg = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main"
value = "Start Page"  # 读取的值
command = 'reg query "%s" /v "%s"' % (reg, value)  # 拼接字符串
proxy = os.popen(command)  # 执行命令，返回通道的代理文件流
result = proxy.read()  # 读取文件流中的内容
line = str(result.splitlines()[2])  # 将三行内容转为文本
values = line.split()  # 按照空白内容分割
print("IE浏览器的默认主页为：" + values[-1])  # 打印最后一个元素值
