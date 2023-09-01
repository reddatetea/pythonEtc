import os

width = "1024"  # 屏幕宽度
height = "768"  # 屏幕高度

# 修改注册表作用war3游戏的屏幕分辨率宽度
reg_com_1 = 'reg add "HKEY_CURRENT_USER\Software\Blizzard Entertainment\Warcraft III\Video" /v reswidth /t REG_DWORD /d %s /f' % width
# 修改注册表作用war3游戏的屏幕分辨率高度
reg_com_2 = 'reg add "HKEY_CURRENT_USER\Software\Blizzard Entertainment\Warcraft III\Video" /v resheight /t REG_DWORD /d %s /f' % height

result1 = os.system(reg_com_1)  # 修改注册表
result2 = os.system(reg_com_2)
if result1 + result2 == 0:  # 如果两个命令都执行成功
    print("修改成功，war3游戏界面改为%s*%s" % (width, height))
else:
    print("修改失败s")
