import sys
print(sys.getcheckinterval()) # 输出默认检查间隔
sys.setcheckinterval(10) # 手动设置检查间隔为10
print(sys.getcheckinterval()) # 输出设置完的检查间隔