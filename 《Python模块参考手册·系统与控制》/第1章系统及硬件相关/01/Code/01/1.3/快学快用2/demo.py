import os
old_file = "D:\\test\\demo.mp4"  # 原始视频文件
new_file = "D:\\test\\part.mp4"  # 转换之后的文件
start_time = "00:01:00"  # 片段在原视频中开始的时间
end_time = "00:01:15"  # 片段在原视频中结束的时间
# 参数写在列表里
avg = ["ffmpeg", "-i", old_file, "-vcodec", "copy", "-acodec", "copy", "-ss", start_time, "-to", end_time, new_file, "-y"]
# 第一个参数为ffmpeg.exe完整名，第二个参数为其他参数列表
os.execv("D:\\test\\ffmpeg.exe", avg)
