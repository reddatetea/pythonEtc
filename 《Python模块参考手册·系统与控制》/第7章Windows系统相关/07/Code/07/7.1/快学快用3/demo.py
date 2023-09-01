import sys
__SP = sys.getwindowsversion()[4]    # 获取补丁信息
if __SP=='':
    print('当前系统没有安装任何补丁')
else:
    print('当前系统已经安装了 %s 补丁' %(__SP))