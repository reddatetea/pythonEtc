import os
old_file = "D:\\test\\demo.mp4"  # 原视频文件
new_file = "D:\\test\\demo.mp3"  # 转换之后的音频文件
# 第一个参数为ffmpeg.exe完整名，第二个参数为ffmpeg，后面接其他参数
os.execl("D:\\test\\ffmpeg.exe", "ffmpeg", "-i", old_file, "-f", "mp3", "-vn", new_file, "-y")
