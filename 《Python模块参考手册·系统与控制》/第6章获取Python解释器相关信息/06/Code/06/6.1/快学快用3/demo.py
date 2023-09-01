import sys
__RELEASELEVEL = sys.version_info[3]#获取Python版本级别
if __RELEASELEVEL == "alpha":#判断版本级别是否为alpha
    print("内测版")
elif __RELEASELEVEL == "beta":#判断版本级别是否为beta
    print("公测版")
elif __RELEASELEVEL == "candidate":#判断版本级别是否为candidate
    print("候选版")
else:
    print("最终版")