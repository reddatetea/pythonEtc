import sys
dianXin = [133, 149, 153, 173, 177, 180, 181, 189, 191, 199] # 运营商为中国电信的号段
# 运营商为中国联通的号段
lianTong = [130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186]
yiDong = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158,
          159, 172, 178, 182, 183, 184, 187, 188, 198] # 运营商为中国移动的号段
print('请输入手机号：')
# 读取并且把用户输入的手机号中的前3个字符转换为int
firstThreeNum = int(sys.stdin.read(3))
for i in range(len(dianXin)): # 遍历中国电信的号段
    if firstThreeNum == dianXin[i]:
        print('这个手机号的运营商是中国电信')
        break
for j in range(len(lianTong)): # 遍历中国联通的号段
    if firstThreeNum == lianTong[j]:
        print('这个手机号的运营商是中国联通')
        break
for k in range(len(yiDong)): # 遍历中国移动的号段
    if firstThreeNum == yiDong[k]:
        print('这个手机号的运营商是中国移动')
        break