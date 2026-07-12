import platform
if platform.system() == "Windows":
    import os
    os.system("movie.mp4")
if platform.system() == "Darwin":
    import moviepy.editor
    clip = moviepy.editor.VideoFileClip('movie.mp4')
    clip= clip.resize(newsize=(1280,720))
    clip.preview()