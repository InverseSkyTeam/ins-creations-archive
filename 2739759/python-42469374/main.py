import platform
print("""该视频可以在B站上观看,社区版本有所压缩
a.社区观看(macOS用户请先安装moviepy库)
b.B站观看(记得三连)""")
choice = input("请选择:")
if "a" in choice or "A" in choice:
    if platform.system() == "Windows":
        import os
        os.system("Electropop.mp4")
    if platform.system() == "Darwin":
        import moviepy.editor,pygame
        pygame.display.set_caption("Electropop")
        clip = moviepy.editor.VideoFileClip('Electropop.mp4')
        clip= clip.resize(newsize=(1280,720))
        clip.preview()
if "b" in choice or "B" in choice:
    import webbrowser
    webbrowser.open("https://www.bilibili.com/video/BV148411c72B/?spm_id_from=333.999.0.0&vd_source=803ca6df885b8ec2a54516db3bd9d282", new=0, autoraise=True)