import moviepy.editor
clip = moviepy.editor.VideoFileClip('tk窗口制作器.3GP')
clip= clip.resize(newsize=(1280,720))
clip.preview()