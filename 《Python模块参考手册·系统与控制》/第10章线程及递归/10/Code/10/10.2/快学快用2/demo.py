import sys
sys.setswitchinterval(4294.9) # 手动设置线程间隔为最大值
print('4294.9'+':'+str(sys.getswitchinterval())) # 输出设置完的线程间隔
sys.setswitchinterval(4295) # 手动设置线程间隔超过4294.9
print('4295'+':'+str(sys.getswitchinterval())) # 输出设置完的线程间隔
sys.setswitchinterval(8888) # 手动设置线程间隔超过4294.9
print('8888'+':'+str(sys.getswitchinterval())) # 输出设置完的线程间隔