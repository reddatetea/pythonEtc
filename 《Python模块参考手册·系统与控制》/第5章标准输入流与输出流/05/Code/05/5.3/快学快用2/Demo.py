import sys
import random
target_Num = random.randint(1, 100) # 读取一个在1~99范围内的随机数作为目标数字
input_Num = 0 # 初始化用户输入的数字为0
input_Times = 1 # 初始化用户输入的次数为1
# 用户输入的数字与目标数字不相等，并且用户输入的次数不满6次
while input_Num != target_Num and input_Times < 7:
    print('请输入一个在1~99氛围内的数字：')
    input_Num = int(sys.stdin.readline()) # 用户输入的数字
    if input_Num < target_Num: # 用户输入的数字小于目标数字
        print('输入的数字太小了')
    elif input_Num > target_Num: # 用户输入的数字大于目标数字
        print('输入的数字太大了')
    input_Times += 1 # 用户输入的次数加1
if input_Num == target_Num: # 用户输入的数字与目标数字相等
    print('真棒，恭喜你猜中了')
else:
    print('你用光了所有机会，目标数字是' + str(target_Num))