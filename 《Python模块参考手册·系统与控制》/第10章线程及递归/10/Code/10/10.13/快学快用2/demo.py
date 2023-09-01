import sys
list=sys.get_asyncgen_hooks() # 使用列表存储asyncgen_hooks对象
# 格式化输出
print('firstiter={0}\nfinalizer={1}'.format(list[0],list[1]))