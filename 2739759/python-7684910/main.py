from moviepy.editor import *
clip = VideoFileClip('华晨宇-我管你 (真我版) (百龄坛特醇 #活出真我#推广曲)(标清).mp4')
clip= clip.resize(newsize=(1024,600))
clip.preview()