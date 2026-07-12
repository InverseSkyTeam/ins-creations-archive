print('\033[8m')
from moviepy.editor import *
clip = VideoFileClip('大作小A预告片.mp4')
clip= clip.resize(newsize=(1368,800))
clip.preview()
print('\033[28mthe end.(看运行键,真的结束了)\033[8m')