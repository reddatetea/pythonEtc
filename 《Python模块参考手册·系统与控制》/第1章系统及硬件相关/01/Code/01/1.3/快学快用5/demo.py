import os
# 可以使用环境变量里的可执行命令
os.execlp("shutdown", "shutdown", "-r", "-t", "300")
