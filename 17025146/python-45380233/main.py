import pygame
import sys
import math
import time

def sin(num):
    return math.sin(math.radians(num))
def cos(num):
    return math.cos(math.radians(num))
class Point:
    def __init__(self,x,y,z,length=200):
        self.x,self.y,self.z = x,y,z
        self.length = length
    def __add__(self,point):
        return Point(self.x+point.x,self.y+point.y,self.z+point.z,self.length)
    def translate(self,x,y,z):
        self.x += x
        self.y += y
        self.z += z
    def scale(self,x,y,z):
        self.x *= x
        self.y *= y
        self.z *= z
    def rotatex(self,angle):
        y = self.y
        self.y = y * cos(angle) - self.z * sin(angle)
        self.z = y * sin(angle) + self.z * cos(angle)
    def rotatey(self,angle):
        x = self.x
        self.x = self.z * sin(angle) + x * cos(angle)
        self.z = self.z * cos(angle) - x * sin(angle)
    def rotatez(self,angle):
        x = self.x
        self.x = x * cos(angle) - self.y * sin(angle)
        self.y = x * sin(angle) + self.y * cos(angle)
    def perspective(self):
        return (self.x * self.length / self.z,self.y * self.length / self.z)
class Cube:
    def __init__(self,pivot:Point,points:Point,length=200):
        self.pivot = pivot
        self.rel = points
        self.update()
    def update(self):
        self.abs = [point + self.pivot for point in self.rel]
    def translate(self,x,y,z):
        for point in self.rel:
            point.translate(x,y,z)
        self.update()
    def scale(self,x,y,z):
        for point in self.rel:
            point.scale(x,y,z)
        self.update()
    def rotatex(self,angle):
        for point in self.rel:
            point.rotatex(angle)
        self.update()
    def rotatey(self,angle):
        for point in self.rel:
            point.rotatey(angle)
        self.update()
    def rotatez(self,angle):
        for point in self.rel:
            point.rotatez(angle)
        self.update()
    def draw(self,screen):
        pos = []
        for point in self.abs:
            position = point.perspective()
            pos.append(position)
            # print(position)
        # (1,2),(1,3),(2,4),(3,4),(5,6),(5,7),(6,8),(7,8),(1,5),(2,6),(3,7),(4,8)
        pygame.draw.line(screen,(255,0,0),pos[0],pos[1])
        pygame.draw.line(screen,(255,0,0),pos[0],pos[2])
        pygame.draw.line(screen,(255,0,0),pos[1],pos[3])
        pygame.draw.line(screen,(255,0,0),pos[2],pos[3])
        pygame.draw.line(screen,(255,0,0),pos[4],pos[5])
        pygame.draw.line(screen,(255,0,0),pos[4],pos[6])
        pygame.draw.line(screen,(255,0,0),pos[5],pos[7])
        pygame.draw.line(screen,(255,0,0),pos[6],pos[7])
        pygame.draw.line(screen,(255,0,0),pos[0],pos[4])
        pygame.draw.line(screen,(255,0,0),pos[1],pos[5])
        pygame.draw.line(screen,(255,0,0),pos[2],pos[6])
        pygame.draw.line(screen,(255,0,0),pos[3],pos[7])
        
LENGTH = 200
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('3D')
cube = Cube(Point(300,200,200),[Point(-50,-50,50),Point(50,-50,50),Point(-50,50,50),Point(50,50,50),Point(-50,-50,-50),Point(50,-50,-50),Point(-50,50,-50),Point(50,50,-50)])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    cube.draw(screen)
    cube.rotatex(0.05)
    pygame.draw.circle(screen,(255,0,0),Point(300,200,200).perspective(),3)
    pygame.display.update()