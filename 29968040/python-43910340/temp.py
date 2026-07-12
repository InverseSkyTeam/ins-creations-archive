def get3d(x,y,z,anglex,angley,anglez):
    def sin(num):
        return math.sin(math.radians(num))
    def cos(num):
        return math.cos(math.radians(num))
    if x!=0:
        y=y*cos(anglex)-z*sin(anglex)
        z=y*sin(anglex)+z*cos(anglex)
    if y!=0:
        x=z*sin(angley)+x*cos(angley)
        z=z*cos(angley)-x*sin(angley)
    if z!=0:
        x=x*cos(anglez)-y*sin(anglez)
        z=x*sin(anglez)+y*cos(anglez)
    return (int(x*350/z),int(y*350/z))
def draw_line_fill(p1,p2,p3,p4,color):
    pygame.draw.aalines(screen,(0,0,0),True,[p1,p2,p3,p4])
    pygame.draw.polygon(screen,color,[p1,p2,p3,p4])
def draw_3d_rect(x,y,z,llong,anglex,angley,anglez,mode,color):
    if mode=='xy':#xy模式，在正面和背面
        p1=get3d(x,y,z,anglex,angley,anglez)
        p2=get3d(x+llong,y,z,anglex,angley,anglez)
        p3=get3d(x+llong,y+llong,z,anglex,angley,anglez)
        p4=get3d(x,y+llong,z,anglex,angley,anglez)
    elif mode=='xz':#xz模式，用于顶面和底面
        p1=get3d(x,y,z,anglex,angley,anglez)
        p2=get3d(x+llong,y,z,anglex,angley,anglez)
        p3=get3d(x+llong,y,z+llong,anglex,angley,anglez)
        p4=get3d(x,y,z+llong,anglex,angley,anglez)
    elif mode=='yz':#yz模式，用于左右面
        p1=get3d(x,y,z,anglex,angley,anglez)
        p2=get3d(x,y+llong,z,anglex,angley,anglez)
        p3=get3d(x,y+llong,z+llong,anglex,angley,anglez)
        p4=get3d(x,y,z+llong,anglex,angley,anglez)
    draw_line_fill(p1,p2,p3,p4,color)
#总长(格子数)，总宽，总高，线长度（单个格子）,data，角度x,y,z,显示x,y
def draw_3drect(hlong,width,height,llong,data,anglex,angley,anglez,myx,myy):
    draw_3d_rect(0,0,0,100,20,0,0,'xy',(255,255,255))
    draw_3d_rect(0,0,0,100,20,0,0,'xz',(255,255,255))


if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #cube.move('left')
                    #bgx-=1
                    k=0
                elif event.key == pygame.K_RIGHT:
                    #cube.move('right')
                    #bgx+=1
                    k=1
                elif event.key == pygame.K_UP:
                    #cube.move('up')
                    #bgy-=1
                    k=2
                elif event.key == pygame.K_DOWN:
                    #cube.move('down')
                    #bgy+=1
                    k=3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    #cube.move('left')
                    #bgx-=1
                    k=-1
                elif event.key == pygame.K_RIGHT:
                    #cube.move('right')
                    #bgx+=1
                    k=-1
                elif event.key == pygame.K_UP:
                    #cube.move('up')
                    #bgy-=1
                    k=-1
                elif event.key == pygame.K_DOWN:
                    #cube.move('down')
                    #bgy+=1
                    k=-1
        if k!=-1:
            if k==0:
                bgx-=1
            elif k==1:
                bgx+=1
            elif k==2:
                bgy-=1
            else:
                bgy+=1
                
                
'''while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #cube.move('left')
                bgx-=1
            elif event.key == pygame.K_RIGHT:
                #cube.move('right')
                bgx+=1
            elif event.key == pygame.K_UP:
                #cube.move('up')
                bgy-=1
            elif event.key == pygame.K_DOWN:
                #cube.move('down')
                bgy+=1
            elif event.key == pygame.K_n:
                n_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                n_down = False
    screen.fill((0,0,0))
    screen.blit(bg, (bgx, bgy))
    #cube.show()
    if cube.get_mode() == 'finish':#当前关卡已结束（当前格子是终点）
        show_text('提示:按下n进入下一个大地',color=(255,228,181),pos=(0,30))
        if n_down:
            n_down = False
            levelindex += 1#关卡编号加一
            startpos = (0,0)
            if levelindex == 2:#在第二关起始位置改为(0,1)
                startpos = (0,1)
            try:
                leveldata = gamedata(levelindex)#获取地图信息
                cube = Cube(leveldata,startpos)#新建地图
            except:#如果获取地图信息时出错，说明通关了，退出主循环
                break
    elif cube.get_mode() == 'goto':#格子是传送门
        show_text('提示:按下n进入传送门',color=(255,228,181),pos=(0,30))
        if n_down:#当按下n键
            n_down = False
            info = cude.data['front'][cube.y][cube.x].info#获取格子传送位置
            cube.x, cube.y = info[1], info[2]
            if info[0] == 'behind':#传送到背面（相对当前面）
                cube.data['left'], cube.data['right'] = cube.data['front'], cube.data['behind']
                cube.data['right'], cube.data['left'] = cube.data['behind'], cube.data['front']
            elif info[0] in ['left','right','up','down']:#传送到其他面
                cube.rotate3d(info[0])#直接换面
    show_text('大地序号:'+str(levelindex),color=(255,228,181),pos=(0,0))
    pygame.display.update()'''

#print('目前的测试关胜利了，感谢测试。你已经拥有了足够过关的聪明。')