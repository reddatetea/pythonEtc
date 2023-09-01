import os
proxy = os.popen('systeminfo')  # 执行命令，返回通道的代理文件流
result = proxy.read()  # 读取文件流中的内容
for line in result.splitlines():  # 将内容按行拆分
    line = str(line).strip()  # 行内容转为字符串，去掉首尾空白
    if "系统启动时间" in line:  # 如果包含"系统启动时间" 字样
        print(line)  # 打印启动时间
        break
