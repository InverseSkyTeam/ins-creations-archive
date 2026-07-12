import platform
if platform.system() == "Windows":
    import os
    os.system("侏罗纪公园预告片1-压缩版.avi")
if platform.system() == "Darwin":
    import moviepy.editor
    clip = moviepy.editor.VideoFileClip('侏罗纪公园预告片1-压缩版.avi')
    clip= clip.resize(newsize=(1280,720))
    clip.preview()