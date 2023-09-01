import os  # 文件与操作系统相关模块
path = os.path.join(os.getenv('JAVA_HOME'), r'bin\jmc.ini')   # 组合配置文件的完整路径
print(path)   # 输出路径
