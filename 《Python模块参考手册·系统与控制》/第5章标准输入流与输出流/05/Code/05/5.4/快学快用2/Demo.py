import sys
temp = sys.stdout
sys.stdout = open('test.txt','w') # sys.stdout的指向将从控制台重定向到文件
print('hello world')
sys.stdout = temp # 恢复sys.stdout的原始指向
print('just do it')