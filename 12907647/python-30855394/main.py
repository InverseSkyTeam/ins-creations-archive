from moviepy.editor import *
clip = VideoFileClip('小轩电脑1.0开机动画.mp4')
clip = clip.resize(newsize=(1200,650))
clip.preview()