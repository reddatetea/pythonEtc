import sys
print('列表：',sys.getsizeof([]))
print('元组：',sys.getsizeof(()))
print('字典：',sys.getsizeof({}))
print('字符串：',sys.getsizeof(''))
print('字节：',sys.getsizeof(b'bytes'))
print('整数：',sys.getsizeof(1))
print('小数：',sys.getsizeof(3.14))