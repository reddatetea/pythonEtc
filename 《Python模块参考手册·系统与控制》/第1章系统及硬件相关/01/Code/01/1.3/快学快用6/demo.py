import os
# 给path环境变量添加Java运行环境的文件夹地址
env = {"PATH": "C:\\Program Files\\Java\\jdk-11.0.2\\bin;"}
# 启动Eclipse的命令
args = ["eclipse.exe"]
# 指定Eclipse的启动文件，启动Eclipse，同时配置临时环境变量，
os.execve("E:\\eclipse\\eclipse.exe", args, env)
