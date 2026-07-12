def ImageToChar(filename,fontname,savename,w=100,h=100):
    
    if w<80 or h<80:
        big=10
    elif w<100 or h<100:
        big=8
    elif w<150 or h<150:
        big=6
    elif w<200 or h<200:
        big=4
    elif w<=300 or h<=300:
        big=2
    else:
        print("width is too big . Please let it under the number 300.")
    try:
        from PIL import Image
    except:
        from Pillow import Image
    import pygame,sys,os
    
    pygame.init()
    
    # 字符画使用的字符集
    
    char = list("$@B%8$@B%8&W$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ^`'. ^`'. ^`'. ")
    
    def get_char(r,g,b,alpha = 256):
    
      #将256灰度映射到n个字符上
    
      if alpha == 0:
    
        return ' '
    
      length = len(char)
    
      # 计算灰度的公式
    
      gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
      level = (256.0 + 1)/length
    
      index=int(gray/level)
    
      return char[index]
    
    
    p = Image.open(filename)
    
    width=p.size[0]
    height=p.size[1]
    s=1.1
    
    while(width>w and height>h):
        width/=s
        height/=s
    
    width=int(width)
    height=int(height)#-10
    
    #print(p.size)
    photo = p.resize((width,height),Image.NEAREST)#生成npx*npx长宽的低质量图片
    #print(photo.size)
    
    
    txt = ""
    listofchr=[]
    # 获取每个像素点对应的字符
    
    for i in range(height):
    
        for j in range(width):
        
            txt += get_char(*photo.getpixel((j,i)))#获取每个像素点
            txt+=' '
        listofchr.append(txt)
        txt = ''
        
    for i in range(height):
        print(listofchr[i])
        
    
    #字符画输出到文件
    
    with open("output.txt",'w') as f:
        for i in range(height):
            f.write(listofchr[i])
            f.write('\n')
        
        
        
        
    
    screen = pygame.display.set_mode((2*width*big+40,height*big+20))
    pygame.display.set_caption("IMAGE字符化")
    ifont1=pygame.font.Font(fontname,big)
    
    itext1=ifont1.render(" ",True,(50,50,50))
    x=20
    y=20
    while True:
        screen.fill((255,255,255))
        for i in range(height):
            itext1=ifont1.render(listofchr[i],True,(50,50,50))
            screen.blit(itext1,(x,y))
            y+=big
        y=big
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(pygame.display.get_surface(),savename)
                os.system(savename)
                pygame.quit()
                sys.exit()
        pygame.display.update()


        
def ImageToTxt(filename,w=100,h=100):
    if w<80 or h<80 :
        big=10
    elif w<100 or h<100 :
        big=8
    elif w<150 or h<150 :
        big=6
    elif w<200 or h<200 :
        big=4
    elif w<=300 or h<=300 :
        big=2
    else:
        print("width is too big . Please let it under the number 300.")
    try:
        from PIL import Image
    except:
        from Pillow import Image
    import pygame,sys,os
    
    pygame.init()
    
    # 字符画使用的字符集
    
    char = list("$@B%8$@B%8&W$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ^`'. ^`'. ^`'. ")
    
    def get_char(r,g,b,alpha = 256):
    
      #将256灰度映射到n个字符上
    
      if alpha == 0:
    
        return ' '
    
      length = len(char)
    
      # 计算灰度的公式
    
      gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
      level = (256.0 + 1)/length
    
      index=int(gray/level)
    
      return char[index]
    
    
    p = Image.open(filename)
    
    width=p.size[0]
    height=p.size[1]
    s=1.1
    
    while(width>w and height>h):
        width/=s
        height/=s
    
    width=int(width)
    height=int(height)#-10
    
    photo = p.resize((width,height),Image.NEAREST)#生成npx*npx长宽的低质量图片

    txt = ""
    listofchr=[]
    # 获取每个像素点对应的字符
    
    for i in range(height):
    
        for j in range(width):
        
            txt += get_char(*photo.getpixel((j,i)))#获取每个像素点
            txt+=' '
        listofchr.append(txt)
        txt = ''
    return listofchr


def ImageLevel(filename,w=100,h=100):
    try:
        from PIL import Image
    except:
        from Pillow import Image

    if w<80 or h<80 :
        big=10
    elif w<100 or h<100 :
        big=8
    elif w<150 or h<150 :
        big=6
    elif w<200 or h<200 :
        big=4
    elif w<=300 or h<=300 :
        big=2
    p = Image.open(filename)
    
    width=p.size[0]
    height=p.size[1]
    s=1.1
    
    while(width>w and height>h):
        width/=s
        height/=s
    
    width=int(width)
    height=int(height)#-10

    return (width,height,big)





def VideoToChar( filename,fontname,jianame,beishu,big,w=100,h=100,music="none"):
    import cv2,os,time,DrawChar

    videoPath=filename
    # 视屏获取
    v=cv2.VideoCapture(videoPath)
    # 帧率(frames per second)
    fps = v.get(cv2.CAP_PROP_FPS)
    # 总帧数(frames)
    frames = v.get(cv2.CAP_PROP_FRAME_COUNT)
    
    #print("帧数："+str(fps))
    #print("总帧数："+str(frames))
    #print("视屏总时长："+"{0:.2f}".format(frames/fps)+"秒")
    
    time.sleep(2)
    
    ret=True
    count=0
    
    yujiframes=frames//beishu
    
    while True:
        ret,frame = v.read()
        if ret is True:
            if count%beishu==0:
                #frame=frame[10:height,0:width]截取大小
                name="./ImageData/fps"+str(int((count+1)/beishu))+".png"
                cv2.imwrite(name, frame)
                print(str(int((count+1)/beishu/yujiframes*100))+"%|",end=" ")
            count+=1
        else:
            break
    print("逐帧导出成功")
    
    all_fps_list=[]
    
    for i in range (int((count+1)/beishu)):
        filename="./"+jianame+"/fps"+str(i)+".png"
        all_fps_list.append(ImageToTxt(filename,w,h))
        if i==0:
            www=ImageLevel(filename,w,h)[0]
            hhh=ImageLevel(filename,w,h)[1]
            bbbig=ImageLevel(filename,w,h)[2]
        print(str(i/int((count+1)/beishu)*100)+"|",end=" ")
    if big!=0:
        bbbig=big
        
        
    import pygame,sys
        
    pygame.init()
    screen = pygame.display.set_mode((2*www*bbbig+40,hhh*bbbig+20))
    pygame.display.set_caption("IMAGE字符化")

    ifont1=pygame.font.Font(fontname,bbbig)
            
    itext1=ifont1.render(" ",True,(50,50,50))
    x=20
    y=20
    if music!='none':
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.15)
    
    while True:
            screen.fill((255,255,255))
            for j in range(len(all_fps_list)):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                for i in range(hhh):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    itext1=ifont1.render(all_fps_list[j][i],True,(50,50,50))
                    screen.blit(itext1,(x,y))
                    y+=bbbig
                pygame.display.update()
                pygame.time.wait(150)
                screen.fill((255,255,255))
                
                x=20
                y=20
                itext1=ifont1.render(" ",True,(50,50,50))
                if j==len(all_fps_list)-1:
                    j=0
