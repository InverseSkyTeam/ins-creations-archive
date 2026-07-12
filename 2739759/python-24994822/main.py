import platform
if platform.system() == "Windows":
    import os
    os.system("侏罗纪公园.mp4")
if platform.system() == "Darwin":
    import moviepy.editor
    clip = moviepy.editor.VideoFileClip('侏罗纪公园.mp4')
    clip= clip.resize(newsize=(1280,720))
    clip.preview()