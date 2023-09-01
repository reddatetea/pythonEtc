import sys
version_info = sys.version_info     #获取Python版本信息
name = ["主版本号","次版本号","生成号","版本级别","修订号"]
len = len(version_info)             #获取元素个数
for n in range(len):
    print(name[n],":",version_info[n])#打印版本信息