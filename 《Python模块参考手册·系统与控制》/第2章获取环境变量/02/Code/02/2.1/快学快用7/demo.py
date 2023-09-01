import os
digits = os.getenv("PROCESSOR_ARCHITECTURE")  # 读取当前处理器架构
if digits == "AMD64":
    print("64位系统")
elif digits == "x86":
    print("32位系统")
else:
    print("无法识别系统位数")
