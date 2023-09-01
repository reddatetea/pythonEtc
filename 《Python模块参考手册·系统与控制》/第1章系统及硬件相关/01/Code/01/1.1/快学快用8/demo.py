import os

soft_name = set()  # 已安装软件名称集合

def read_reg(reg):  # 读取软件注册表，获取软件名
    command = 'reg query "%s" /v "DisplayName"' % reg
    proxy = os.popen(command)  # 执行命令，返回通道的代理文件流
    result = proxy.read()  # 读取文件流中的内容
    lines = result.splitlines()  # 将内容按行拆分，保存成对象
    for i in range(0, len(lines)):  # 遍历行索引
        line = str(lines[i]).strip()  # 将一个行内容转为字符串，去除两边空白
        if line == reg:  # 如果这一行内容与软件注册表项相同
            next_line = str(lines[i + 1]).strip()  # 获取将下一行的文本内容
            values = next_line.split()  # 按照空白内容分割
            name = " ".join(values[2:])  # 将前两项以外的元素拼接成字符串
            return name  # 拼接出的字符串就是软件全名

# 软件安装列表注册表项
command = "reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall"
proxy = os.popen(command)  # 执行命令，返回通道的代理文件流
result = proxy.read()  # 读取文件流中的内容

for soft_reg in result.splitlines():  # 将内容按行拆分
    if len(soft_reg) == 0:  # 如果这一行没有任何内容
        continue  # 跳过，读下一行
    soft_reg = str(soft_reg)  # 转为字符串
    name = read_reg(soft_reg)  # 根据注册表项内容获取出软件的名称
    if name is not None:  # 如果能够读到有效内容
        soft_name.add(name)  # 放到软件名称集合中

print("您电脑已安装的软件有：")
for name in soft_name:
    print(name)
