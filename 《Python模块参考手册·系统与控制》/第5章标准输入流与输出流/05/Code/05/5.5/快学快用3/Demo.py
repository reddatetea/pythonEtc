import sys      #  调入系统模块
sys.stdout = open('mingri.txt','w')
sys.stdout.write('hello world ')