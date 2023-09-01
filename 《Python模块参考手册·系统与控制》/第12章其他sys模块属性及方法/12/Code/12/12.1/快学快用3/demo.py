import sys
print('模块列表：')
for i in sys.modules.keys(): # 遍历模块列表
    print(' '+i) # 输出模块