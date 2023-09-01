import sys
print(sys.getswitchinterval()) # 输出默认线程间隔
sys.setswitchinterval(0.1) # 手动设置线程间隔为0.1秒
print(sys.getswitchinterval()) # 输出设置完的线程间隔