import sys
print('参数为1：',sys.getrefcount(1))
print('参数为256：',sys.getrefcount(256))
print('参数为257：',sys.getrefcount(257))
print('参数为1111111：',sys.getrefcount(1111111))
print('参数为-5439：',sys.getrefcount(-5439))