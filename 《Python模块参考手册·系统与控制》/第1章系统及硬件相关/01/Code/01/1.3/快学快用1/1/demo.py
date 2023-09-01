import os
old_file = "D:\\test\\demo.mp4"  # 原始视频文件
new_file = "D:\\test\\demo.flv"#转换之后的文件
# 第一个参数为ffmpeg.exe完整名，第二个参数为ffmpeg，后面接其他参数
os.execl("D:\\test\\ffmpeg.exe", "ffmpeg", "-i", old_file, "-vcodec", "copy", "-acodec", "copy", new_file, "-y")
