#选用库
import pygame
import DrawLib #导入绘图库
from random import randint #导入随机数函数
import time #导入时间模块

#必用库
from SimplyVector import SimplyVector #导入平面向量类
from SimplyBody import SimplyBody #导入平面刚体类
from SimplyWorld import SimplyWorld


pygame.init()
#初始化
#初始化绘图
gwidth = 400
gheight=300
screen = pygame.display.set_mode((gwidth, gheight))
graphics = DrawLib.Window(screen, gwidth, gheight) 
outline = (255, 255, 255)

#初始化世界
world = SimplyWorld()

def create_wall(width, height):
    return SimplyBody.CreateBoxBody(
        width, 
        height,
        Density = 1,
        IsStatic = True,
        Restitution = 0.5,
        InherentStaticFriction = 1,
        InherentDynamicFriction = 0.8
    ) 

def create_circle(radius):
    return SimplyBody.CreateCircleBody(
        radius,
        Density = 10,
        IsStatic = False,
        Restitution = 0.5,
        InherentStaticFriction = 1,
        InherentDynamicFriction = 0.8
    )

body = create_wall(gwidth-40, 10)
body[1].MoveTo(SimplyVector(200,280))
world.AddBody(body[1])

body = create_wall(130, 10)
body[1].MoveTo(SimplyVector(80,150))
body[1].RotateTo(3.1415926/6)
world.AddBody(body[1])

body = create_wall(130, 10)
body[1].MoveTo(SimplyVector(250,100))
body[1].RotateTo(-3.1415926/8)
world.AddBody(body[1])

import time
#主函数
def my_main():
    clock = pygame.time.Clock()
    t = 1/120
    while True:
        s=time.time()
        graphics.clear_canvas()

        #创建物体并添加到世界
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                Position = SimplyVector(*event.pos)
                body = create_circle(randint(5,20))
                body[1].MoveTo(Position)
                world.AddBody(body[1])

        #从世界中获得物体信息并绘制 
        for i in range(world.BodyCount()):
            getOrNot,body = world.GetBody(i)
            if not getOrNot:
                raise Exception("获取物体失败")
            graphics.draw_shape(body)

        world.Step(t, 1)#更新世界

        try:
            for i in range(world.BodyCount()):
                bool_result,body = world.GetBody(i)
                box = body.GetAABB()
                if box.Min.y>gheight:
                    world.RemoveBody(body)
        except:
            continue

        pygame.display.update()
        clock.tick(120)
        t = time.time() - s
