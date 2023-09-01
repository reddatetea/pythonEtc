# encoding=utf-8
import ctypes
import sys

addr = sys.exec_prefix[0:1]  # 获取文件所在磁盘
free_bytes = ctypes.c_ulonglong(0)  # 获取该磁盘的剩余空间
ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(addr + ":\\"), None, None, ctypes.pointer(free_bytes))
print("Python安装文件在", addr, "盘，并且", addr, "盘中还有", free_bytes.value / 1024 / 1024 / 1024, "GB剩余空间")
