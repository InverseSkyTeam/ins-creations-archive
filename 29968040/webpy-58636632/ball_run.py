import math
import random
from ball import Ball
import pygame
import pygame.image
import pygame.music
import time
from merge_animal import MergeAnimal
from ball_data import BallData


ballData = [
    BallData(
        radius=125,
        cor=0.2,
        img="icon/ball1.png",
        merge_img="icon/merge2.png"
    ),
    BallData(
        radius=115,
        cor=0.3,
        img="icon/ball2.png",
        merge_img="icon/merge3.png",
    ),
    BallData(
        radius=105,
        cor=0.3,
        img="icon/ball3.png",
        merge_img="icon/merge4.png",
    ),
    BallData(
        radius=95,
        cor=0.3,
        img="icon/ball4.png",
        merge_img="icon/merge5.png",
    ),
    BallData(
        radius=80,
        cor=0.3,
        img="icon/ball5.png",
        merge_img="icon/merge6.png",
    ),
    BallData(
        radius=70,
        cor=0.3,
        img="icon/ball6.png",
        merge_img="icon/merge7.png",
    ),
    BallData(
        radius=60,
        cor=0.3,
        img="icon/ball7.png",
        merge_img="icon/merge8.png",
    ),
    BallData(
        radius=50,
        cor=0.3,
        img="icon/ball8.png",
        merge_img="icon/merge9.png",
    ),
    BallData(
        radius=40,
        cor=0.3,
        img="icon/ball9.png",
        merge_img="icon/merge10.png",
    ),
    BallData(
        radius=30,
        cor=0.3,
        img="icon/ball10.png",
        merge_img="icon/merge11.png",
    ),
    BallData(
        radius=20,
        cor=0.1,
        img="icon/ball11.png",
        merge_img="icon/merge11.png",
    )
]


width, height = 800, 600
finish = 0
score = 0
lineDashY = 100
preBallLeaveDate = time.time()

balls = []
currentBall = None
downSound = None
mergeSound1 = None
mergeSound2 = None
finishSound = None


def load_sound():
    global downSound, mergeSound1, mergeSound2, finishSound
    downSound = pygame.music.load('audio/down.wav')
    mergeSound1 = pygame.music.load('audio/merge1.wav')
    mergeSound2 = pygame.music.load('audio/merge2.wav')
    finishSound = pygame.music.load('audio/finish.wav')


def get_ball_data():
    if len(balls) < 3:  # 开场前3个都为葡萄
        return len(ballData) - 1

    elif len(balls) < 6:
        if random.random() < 0.55:
            return len(ballData) - 1
        if random.random() < 0.55:
            return len(ballData) - 2
        if random.random() < 0.88:
            return len(ballData) - 3
        if random.random() < 0.77:
            return len(ballData) - 4
        if random.random() < 0.66:
            return len(ballData) - 5
        return len(ballData) - 6

    else:
        if random.random() < 0.35:
            return len(ballData) - 1
        if random.random() < 0.25:
            return len(ballData) - 2
        if random.random() < 0.36:
            return len(ballData) - 3
        if random.random() < 0.40:
            return len(ballData) - 4
        return len(ballData) - 5


def newBall(x):
    global currentBall
    index = get_ball_data()
    ball_data = ballData[index]

    if x < ball_data.radius:
        x = ball_data.radius
    elif x + ball_data.radius > width:
        x = width - ball_data.radius

    dynamic_object = Ball()
    dynamic_object.pointX = x
    dynamic_object.pointY = ball_data.radius
    dynamic_object.r = ball_data.radius
    dynamic_object.cor = ball_data.cor
    dynamic_object.source = ball_data.img
    dynamic_object.mass = ball_data.radius ** 2
    dynamic_object.ballType = index
    dynamic_object.merge_img = ball_data.merge_img
    dynamic_object.set_width(ball_data.radius * 2)
    dynamic_object.set_height(ball_data.radius * 2)
    currentBall = dynamic_object


def currentBallMove(x):
    global currentBall
    if currentBall is None:
        return False
    if x < currentBall.r or x + currentBall.r > width:
        return False
    currentBall.pointX = x
    return True


def currentBallMove1(x):
    global currentBall
    if currentBall is None:
        return
    if x < currentBall.r:
        x = currentBall.r
    elif x + currentBall.r > width:
        x = width - currentBall.r
    currentBall.pointX = x


def currentBallStartDown():
    global currentBall
    if currentBall is None:
        return False

    if currentBall.shapeChange:
        return False

    currentBall.vy = 10
    balls.append(currentBall)
    currentBall = None
    return True


edgeCorX = 0.2
edgeCorY = 0.2
ballAy = 1


def ballsMove():
    for ball in balls:
        vx, vy = ball.vx, ball.vy
        px, py = ball.pointX, ball.pointY
        r = ball.r
        
        vy += ballAy
        
        ball.preX = px
        ball.preY = py

        px += vx
        py += vy
        

        if px < r:  # 碰到左边墙
            px = r
            vx = -vx * edgeCorX
            if abs(vx) < 0.1:
                vx = 0
        elif px + r > width:  # 碰到右边墙
            px = width - r
            vx = -vx * edgeCorX
            if abs(vx) < 0.1:
                vx = 0

        if py < r:
            py = r
            vy = -vy * edgeCorY
        elif py + r > height:  # 到地面
            ballIsDown(vy)
            py = height - r
            vy = -vy * edgeCorY

        if abs(py + r - height) <= 0.01:
            vx *= 0.97
        
        ball.pointX, ball.pointY = px, py
        ball.vx, ball.vy = vx, vy
        


def collide():
    global balls
    for i in range(len(balls)):
        ball1 = balls[i]
        for j in range(i + 1, len(balls)):
            ball2 = balls[j]
            distance = math.sqrt((ball1.pointX - ball2.pointX) ** 2 + (ball1.pointY - ball2.pointY) ** 2)
            radius = ball1.r + ball2.r

            if distance > radius:
                continue

            if not ball1.mergeStart and not ball2.mergeStart and ball1.ballType == ball2.ballType and ball2.ballType > 0:
                mergeBall(j, i)
                return
            else:
                changeSpeedAndDirection(ball1, ball2, distance, radius)


def ballsRotate():
    global balls
    for ball in balls:
        if ball.mergeStart:
            continue
        distance = math.sqrt((ball.pointX - ball.preX) ** 2 + (ball.pointY - ball.preY) ** 2)

        if abs(distance) and ball.vy < 10:
            if ball.vx > 0:
                ball.rotate += 360 / (2 * ball.r * math.pi) * distance
            else:
                ball.rotate -= 360 / (2 * ball.r * math.pi) * distance
            if abs(ball.vx) < 0.1:
                ball.vx = 0


def changeSpeedAndDirection(ball1, ball2, distance, radius):
    m_1, m_2 = ball1.mass, ball2.mass
    px_1, py_1 = ball1.pointX, ball1.pointY
    px_2, py_2 = ball2.pointX, ball2.pointY
    vx_1, vy_1 = ball1.vx, ball1.vy
    vx_2, vy_2 = ball2.vx, ball2.vy

    if distance < radius:
        # dd = radius - distance
        offsetC = (radius - distance) / radius
        ballOffsetX = (px_1 - px_2) * offsetC
        ballOffsetY = abs((py_1 - py_2) * offsetC)

        px_1 += ballOffsetX * m_2 / (m_1 + m_2)
        px_2 -= ballOffsetX * m_1 / (m_1 + m_2)
        if py_1 > py_2:
            py_2 -= ballOffsetY
        else:
            py_1 -= ballOffsetY

    ex = (px_1 - px_2) / radius
    ey = (py_1 - py_2) / radius

    v1n = ex * vx_1 + ey * vy_1
    v2n = ex * vx_2 + ey * vy_2
    if v1n >= v2n:
        ball1.pointX, ball1.pointY = px_1, py_1  # 这个bug修了好久...
        ball2.pointX, ball2.pointY = px_2, py_2
        ball1.vx, ball1.vy = vx_1, vy_1
        ball2.vx, ball2.vy = vx_2, vy_2
        return
    v1nn = ball1.cor * ((m_1 - m_2) * v1n + 2 * m_2 * v2n) / (m_1 + m_2)
    v2nn = ball2.cor * ((m_2 - m_1) * v2n + 2 * m_1 * v1n) / (m_1 + m_2)

    v1t = ex * vy_1 - ey * vx_1
    v2t = ex * vy_2 - ey * vx_2

    vx_1 = v1nn * ex - v1t * ey
    vy_1 = (v1nn + v1t) * ex

    vx_2 = v2nn * ex - v2t * ey
    vy_2 = (v2nn + v2t) * ex

    if v1n == 0 and v1t == 0 and v2t == 0:
        vx_2 += 0.1
        vy_2 += 0.3
    
    ball1.pointX, ball1.pointY = px_1, py_1
    ball2.pointX, ball2.pointY = px_2, py_2
    ball1.vx, ball1.vy = vx_1, vy_1
    ball2.vx, ball2.vy = vx_2, vy_2



def mergeBall(i, j):
    global score
    ball1 = balls[i]
    ball2 = balls[j]
    new_radius = ballData[ball1.ballType - 1].radius

    ex = ball1.pointX + (ball2.pointX - ball1.pointX) / 2
    ey = ball1.pointY + (ball2.pointY - ball1.pointY) / 2

    if ball1.vy > 10:
        ball1.vy = 0

    if ex < new_radius:
        ex = new_radius
    elif ex + new_radius > width:
        ex = width - new_radius

    if ey < new_radius:
        ey = new_radius
    elif ey + new_radius > height:
        ey = height - new_radius

    ball2.destroy()
    del balls[j]

    score += (len(ballData) - ball1.ballType) * 2
    # print(score)
    ball1.endPointX = ex
    ball1.endPointY = ey
    ball1.ballType -= 1
    ball1.merge_img = ballData[ball1.ballType].merge_img

    r = ball1.r = ballData[ball1.ballType].radius
    ball1.cor = ballData[ball1.ballType].cor
    ball1.mass = r ** 2
    ball1.source = ballData[ball1.ballType].img
    ball1.set_width(r * 2)
    ball1.set_height(r * 2)
    ball1.vx = 0
    ball1.vy = 0

    ball1.mergeStart = True

    newMergeAnimal(ball1.endPointX, ball1.endPointY, ball1.r, ballData[ball1.ballType].merge_img)


def ballOverflow():
    global currentBall
    for ball in balls:
        if not ball.mergeStart and abs(ball.vy) < 0.3 and abs(ball.vx) < 0.3 and ball.y < lineDashY:
            if currentBall is not None:
                balls.append(currentBall)
                currentBall = None
            return True
    return False


def ballCloseAnimal():
    global balls
    minY = 999999
    index = -1

    for i in range(len(balls)):
        ball = balls[i]
        if ball.pointY < minY:
            minY = ball.pointY
            index = i

    if index >= 0:
        image = balls[index].ballType - 1 if balls[index].ballType > 0 else balls[index].ballType

        newMergeAnimal(balls[index].pointX,
                       balls[index].pointY,
                       balls[index].r,
                       ballData[image].merge_img)
        balls[index].destroy()
        del balls[index]

    return index


def pt(a, b):
    now = time.time()
    _t = (now - a)
    if _t>0 and 1 / _t < 250:
        print(b, 1 / _t)
    return now


def process():
    global finish, preBallLeaveDate
    if not finish:
        # a = time.time()
        ballsMove()
        # a = pt(a, 1)
        collide()
        # a = pt(a, 2)
        ballsRotate()
        # a = pt(a, 3)
        
        if ballOverflow():
            finish = 1
        # a = pt(a, 4)
        
    elif finish == 1:
        date = time.time()
        totalMs = date - preBallLeaveDate

        if totalMs > 60 / 1000:
            if ballCloseAnimal() >= 0:
                preBallLeaveDate = date
            else:
                finish = 2
                # finishSound.play()


def newMergeAnimal(pointX, pointY, radius, image):
    MergeAnimal(pointX, pointY, image)
    # mergeSound1.play()
    # mergeSound2.play()
    return True


def ballIsDown(vy):
    # if vy > 30:
    #     downSound.play()
    pass
