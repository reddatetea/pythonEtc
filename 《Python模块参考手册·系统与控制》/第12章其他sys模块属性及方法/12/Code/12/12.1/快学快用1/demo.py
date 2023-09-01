import sys
for k, v in sys.modules.items(): # 遍历所有模块字典
    print(k,':', v) # 输出模块及所在模块文件