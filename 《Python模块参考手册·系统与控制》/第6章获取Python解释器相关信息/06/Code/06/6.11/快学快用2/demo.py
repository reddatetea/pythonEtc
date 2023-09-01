def find_module(module):
    if module in sys.builtin_module_names:  #判断是否是内置模块
        print(module+'是内置模块')
    else:
        print(module+'不是内置模块')
import sys
find_module('os')
find_module('sys')
find_module('string')
find_module('zlib')