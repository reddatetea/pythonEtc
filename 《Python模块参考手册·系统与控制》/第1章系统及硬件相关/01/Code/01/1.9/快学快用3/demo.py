import os
os.system("mode con cols=100 lines=40")              # 自动设置终端宽度和高度
sz = os.get_terminal_size()                           # 获取终端宽度和高度
print(sz)                                               # 输出终端宽度和高度
