import sys
# 检测Windows版本号
__MAJOR, __MINOR, __MICRO = sys.getwindowsversion()[0], sys.getwindowsversion()[1], sys.getwindowsversion()[2]
print('Windows主版本号:' + str(__MAJOR))
print('Windows次版本号:' + str(__MINOR))
print('Windows编译号:' + str(__MICRO))