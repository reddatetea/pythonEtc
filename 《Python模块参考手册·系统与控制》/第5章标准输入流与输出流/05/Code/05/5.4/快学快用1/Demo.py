import sys
sys.stdout = open('test.txt','w') # sys.stdout的指向将从控制台重定向到文件
print('Hello world')