import pygame
import move
move_help='''
这个非线性移动使用了贝塞尔曲线，模仿了css的cubic-bezier
move.cubic_bezier(x,y,x1,y1,time)
！！！特别说明，为了保证一定的精度，所有控制的坐标为css原属性对应坐标的100倍
x:第二个控制点的x坐标（0-100）
y:第二个控制点的y坐标（0-100）
x1:第三个控制点的x坐标（0-100）
y1:第三个控制点的y坐标（0-100）
time:在任务执行的百分比（0-100）
返回在当前 任务执行的百分比 下对应的非线性百分比（返回值在0-100之间，若想变成百分数需要除以100）
比如线性移动时，过去了总移动时间的10%，那么就移动了总移动距离的10%
而非线性移动，则会让此时的移动距离不是总移动距离的10%，从而达到变速效果
示例伪代码（部分）：
import move
起始位置=...
结束位置=...
当前位置=起始位置
for time in range(0,100+1):
    移动总距离=结束位置-起始位置
    当前移动距离=移动总距离*move.cubic_bezier(x,y,x1,y1,time)
    绘制图形（位置=起始位置+当前移动距离）
    刷新屏幕
'''
# 定义常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
x1=20
endx=500
i=0
is_down=0
fx='right'
canxg=0
while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if pygame.mouse.get_pressed()[0] and not is_down:
        is_down=1
        i=0
        if canxg:
            if fx=='left':
               fx='right'
            else:
                fx='left'
    if fx=='right':
        x1=20
        endx=500
    else:
        x1=500
        endx=20
    # 渲染游戏界面
    screen.fill((255, 255, 255))
    x=x1+(endx-x1)*move.cubic_bezier(70,14,57,95,i)/100
    
    if is_down:
        if i<100:
            i+=0.5
        else:
            is_down=0
            canxg=1
    
    #print(x)
    #pygame.draw.rect(screen,(255,255,255),(0,0,800,600))
    pygame.draw.rect(screen, (255, 0, 0), (x, 300, 100, 100))
    pygame.display.flip()

    # 控制游戏帧率
    pygame.time.Clock().tick(60)
