import sys
saveerr = sys.stderr  # 在重定向前保存stderr
# 打开一个新文件用于写入。如果文件不存在，将会被创建。如果文件存在，将被覆盖
info = open('log.txt', 'w')
sys.stderr = info  # 所有后续的错误信息都会被重定向到刚才打开的新文件上
print('change stderr')  # 将错误“打印”到日志文件中
sys.stderr = saveerr  # 重置stderr
info.close()  # 关闭日志文件