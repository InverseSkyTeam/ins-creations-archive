import pygame
from SimplyVector import SimplyVector
from SimplyTransform import SimplyTransform


outline = (255, 255, 255)


class Window:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.bg = (255, 255, 255)
        self.width = width  # 窗口宽度
        self.height = height  # 窗口高度
    
    def clear_canvas(self):
        self.screen.fill(self.bg)

    def draw_line(self, x1, y1, x2, y2, color=(255, 255, 255)):
        pygame.draw.line(self.screen, color, (x1, y1), (x2, y2))
    
    def draw_circle(self, x, y, radius, color=(0, 0, 0), fill=None):
        if fill:
            pygame.draw.circle(self.screen, fill, (x, y), radius)
        pygame.draw.circle(self.screen, color, (x, y), radius, 1)

    def draw_polygon(self, vertices, color=(0, 0, 0), fill=None):
        points = [(i.x, i.y) for i in vertices]
        if fill:
            pygame.draw.polygon(self.screen, fill, points)
        pygame.draw.lines(self.screen, color, True, points)
    
    def draw_shape(self, body):
        if body.ShapeType == "Box":
            if body.IsStatic:
                self.draw_polygon(body.GetTransformedVertices(),color=(255, 0, 0)) 
            else:
                self.draw_polygon(body.GetTransformedVertices(),color=outline) 
        if body.ShapeType == "Circle":
            if body.IsStatic:
                self.draw_circle(body.Position.x,body.Position.y,body.Radius,fill=(0, 0, 0),color=(255, 0, 0)) 
            else:
                va = SimplyVector(0,0)
                vb = SimplyVector(body.Radius,0)
                transform = SimplyTransform(body.Position,body.angle)
                va = SimplyVector.transform(va,transform)
                vb = SimplyVector.transform(vb,transform)                   
                self.draw_circle(body.Position.x,body.Position.y,body.Radius,fill=(0, 0, 0),color=outline) 
                self.draw_line(va.x,va.y,vb.x,vb.y)
