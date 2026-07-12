from moviepy.editor import *
clip = VideoFileClip('乐入人心-帝国进行曲伤情版—纪念大卫·鲍罗斯(超清).mp4')
clip= clip.resize(newsize=(1024,600))
clip.preview()