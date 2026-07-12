import moviepy.editor
clip = moviepy.editor.VideoFileClip('压缩.3GP')
clip= clip.resize(newsize=(1280,720))
clip.preview()