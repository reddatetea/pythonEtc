#encoding=utf-8
import sys
bo=sys.byteorder      #获取本机的字节顺序
if bo=="little":
    print("本机的字节顺序为小端序")
else:
    print("本机的字节顺序为大端序")




