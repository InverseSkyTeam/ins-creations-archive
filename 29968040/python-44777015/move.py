import math,pygame,pygame.gfxdraw
data={
	'ease' :[25,10,25,100],
	'linear' :[0,0,100,100],
	'ease-in' :[42,0,100,100],
	'ease-out' :[0,0,58,100],
	'ease-in-out' :[42,0,58,100],
	'nb':[100,-1054,0,1053]
}
data1=[
	[25,10,25,100],
	[42,0,100,100],
	[0,0,58,100],
	[42,0,58,100],
	[0,0,100,100],
]
#打表降低复杂度
grad_data=[[229, 229, 229] ,[229, 228, 228] ,[229, 228, 228] ,[229, 227, 227] ,[228, 227, 227] ,[228, 227, 226] ,[228, 226, 226] ,[228, 226, 225] ,[228, 225, 225] ,[228, 225, 224] ,[228, 225, 224] ,[227, 225, 223] ,[227,224, 222] ,[227, 224, 222] ,[227, 224, 221] ,[227, 224, 221] ,[227, 223, 220] ,[226, 223, 220] ,[226, 223, 219] ,[226, 223, 219] ,[226, 223, 218] ,[226, 223, 218] ,[226, 223,217] ,[226, 223, 217] ,[225, 223, 216] ,[225, 223, 216] ,[225, 223, 215] ,[225, 223, 214] ,[225, 223, 214] ,[225, 224, 213] ,[224, 224, 213] ,[224, 224, 212] ,[224, 224, 212],[224, 224, 211] ,[223, 224, 211] ,[223, 224, 210] ,[222, 224, 210] ,[221, 223, 209] ,[221, 223, 209] ,[220, 223, 208] ,[219, 223, 208] ,[219, 223, 207] ,[218, 223, 207] ,[217, 223, 206] ,[216, 222, 205] ,[215, 222, 205] ,[215, 222, 204] ,[214,222, 204] ,[213, 222, 203] ,[212, 222, 203] ,[211, 222, 202] ,[210, 221, 202] ,[209, 221, 201] ,[208, 221, 201] ,[207, 221, 200] ,[206, 221, 200] ,[205, 221, 199] ,[204, 220,199] ,[203, 220, 198] ,[201, 220, 198] ,[200, 220, 197] ,[199, 220, 197] ,[198, 220, 196] ,[197, 220, 196] ,[195, 219, 195] ,[195, 219, 195] ,[194, 219, 195] ,[194, 219, 196],[193, 219, 196] ,[193, 219, 196] ,[192, 218, 197] ,[192, 218, 197] ,[191, 218, 197] ,[191, 218, 198] ,[190, 218, 198] ,[190, 218, 199] ,[189, 218, 199] ,[189, 217, 200] ,[188, 217, 200] ,[187, 217, 201] ,[187, 217, 202] ,[186, 217, 202] ,[186,217, 203] ,[185, 217, 203] ,[185, 216, 204] ,[184, 216, 205] ,[184, 216, 206] ,[183, 216, 206] ,[183, 216, 207] ,[182, 216, 208] ,[182, 216, 209] ,[181, 215, 210] ,[181, 215,210] ,[180, 215, 211] ,[180, 215, 212] ,[179, 215, 213] ,[179, 215, 214] ,[178, 214, 214] ,[178, 213, 214] ,[177, 211, 214] ,[177, 210, 214]]
def calc(a,b,c,d,t):
    return a*(1-t)**3+b*3*t*(1-t)**2+c*3*t**2*(1-t)+d*t**3
def cubic_bezier(abcd,x):
    [x1,y1,x2,y2]=abcd
    if x1==y1 and x2==y2:
        return x
    epsilon = 0.0001
    start, end = 0, 1
    P0, P1, P2, P3=0, x1, x2, 100
    while True:
        mid = (start + end) / 2
        point_on_curve = (1 - mid)**3 * P0 + 3 * mid * (1 - mid)**2 * P1 + \
                         3 * mid**2 * (1 - mid) * P2 + mid**3 * P3
        if abs(point_on_curve - x) < epsilon:
            break
        elif point_on_curve > x:
            end = mid
        else:
            start = mid
    t=mid
    return round(calc(0,y1,y2,100,t),6)
class bezier:
    def __init__(self,x0,y0,x1,y1,x2,y2,x3,y3):
        self.x0,self.y0,self.x1,self.y1,self.x2,self.y2,self.x3,self.y3=x0,y0,x1,y1,x2,y2,x3,y3
        self.move=0
        self.point=[]
    def draw(self,screen,line_size,line_color,AuxLine_size,AuxLine_color,point_size,point_color,AuxPoint_size,AuxPoint1_color,AuxPoint2_color,can_border,can_move):
        #绘制辅助线
        pygame.draw.line(screen,AuxLine_color,(self.x0,self.y0),(self.x1,self.y1),AuxLine_size)
        pygame.draw.line(screen,AuxLine_color,(self.x2,self.y2),(self.x3,self.y3),AuxLine_size)
        
        #绘制贝塞尔曲线
        #pygame.gfxdraw.bezier(screen,[(self.x0,self.y0),(self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3)],20,(0,0,0))
        """for i in range(-3,3+1):
            pygame.gfxdraw.bezier(screen,[(self.x0,self.y0-i),(self.x1,self.y1-i),(self.x2,self.y2-i),(self.x3,self.y3-i)],20,(0,0,0))
        """
        point=[]
        for i in range(0,300+1):
            point.append((int(calc(self.x0,self.x1,self.x2,self.x3,i/300)),
            int(calc(self.y0,self.y1,self.y2,self.y3,i/300))))
        pygame.draw.lines(screen,line_color,False,point,line_size)
        #绘制控制点
        pygame.draw.circle(screen,point_color,(self.x0,self.y0),point_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x0,self.y0),point_size,2)
        pygame.draw.circle(screen,point_color,(self.x3,self.y3),point_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x3,self.y3),point_size,2)
        pygame.draw.circle(screen,AuxPoint1_color,(self.x1,self.y1),AuxPoint_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x1,self.y1),AuxPoint_size,2)
        pygame.draw.circle(screen,AuxPoint2_color,(self.x2,self.y2),AuxPoint_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x2,self.y2),AuxPoint_size,2)
        
        if can_move:
            rect1=pygame.Rect(self.x1-AuxPoint_size//2,self.y1-AuxPoint_size//2,AuxPoint_size,AuxPoint_size)
            rect2=pygame.Rect(self.x2-AuxPoint_size//2,self.y2-AuxPoint_size//2,AuxPoint_size,AuxPoint_size)
            if pygame.mouse.get_pressed()[0]:
                if rect1.collidepoint(pygame.mouse.get_pos()) and not self.move:
                    self.move=1
                elif rect2.collidepoint(pygame.mouse.get_pos()) and not self.move:
                    self.move=2
                elif self.move==1 and self.x1<=self.x3 and self.x1>=self.x0:
                    self.x1,self.y1=pygame.mouse.get_pos()
                elif self.move==2 and self.x2<=self.x3 and self.x2>=self.x0:
                    self.x2,self.y2=pygame.mouse.get_pos()
            else:
                self.move=0
        if self.x1>self.x3:
            self.x1=self.x3
        if self.x1<self.x0:
            self.x1=self.x0
        if self.x2>self.x3:
            self.x2=self.x3
        if self.x2<self.x0:
            self.x2=self.x0
    def draw1(self,screen,line_size,line_color,AuxLine_size,AuxLine_color,point_size,point_color,AuxPoint_size,AuxPoint1_color,AuxPoint2_color,can_border,can_move):
        #绘制辅助线
        pygame.draw.line(screen,AuxLine_color,(self.x0,self.y0),(self.x1,self.y1),AuxLine_size)
        pygame.draw.line(screen,AuxLine_color,(self.x2,self.y2),(self.x3,self.y3),AuxLine_size)
        
        #绘制贝塞尔曲线
        if not len(self.point):
            point=[]
            for i in range(0,300+1):
                point.append((int(calc(self.x0,self.x1,self.x2,self.x3,i/300)),
                int(calc(self.y0,self.y1,self.y2,self.y3,i/300))))
            self.point=point
        pygame.draw.lines(screen,line_color,False,self.point,line_size)
        #绘制控制点
        pygame.draw.circle(screen,point_color,(self.x0,self.y0),point_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x0,self.y0),point_size,2)
        pygame.draw.circle(screen,point_color,(self.x3,self.y3),point_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x3,self.y3),point_size,2)
        pygame.draw.circle(screen,AuxPoint1_color,(self.x1,self.y1),AuxPoint_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x1,self.y1),AuxPoint_size,2)
        pygame.draw.circle(screen,AuxPoint2_color,(self.x2,self.y2),AuxPoint_size,0)
        if can_border:
            pygame.draw.circle(screen,(0xb2,0xb2,0xb2),(self.x2,self.y2),AuxPoint_size,2)
        
        if can_move:
            rect1=pygame.Rect(self.x1-AuxPoint_size//2,self.y1-AuxPoint_size//2,AuxPoint_size,AuxPoint_size)
            rect2=pygame.Rect(self.x2-AuxPoint_size//2,self.y2-AuxPoint_size//2,AuxPoint_size,AuxPoint_size)
            if pygame.mouse.get_pressed()[0]:
                if rect1.collidepoint(pygame.mouse.get_pos()) and not self.move:
                    self.move=1
                elif rect2.collidepoint(pygame.mouse.get_pos()) and not self.move:
                    self.move=2
                elif self.move==1 and self.x1<=self.x3 and self.x1>=self.x0:
                    self.x1,self.y1=pygame.mouse.get_pos()
                elif self.move==2 and self.x2<=self.x3 and self.x2>=self.x0:
                    self.x2,self.y2=pygame.mouse.get_pos()
            else:
                self.move=0
        if self.x1>self.x3:
            self.x1=self.x3
        if self.x1<self.x0:
            self.x1=self.x0
        if self.x2>self.x3:
            self.x2=self.x3
        if self.x2<self.x0:
            self.x2=self.x0
    def get_bezier_point(self):
        x1, y1, x2, y2 = self.x1 - self.x0, self.y1 - self.y3, self.x2 - self.x0, self.y2 - self.y3
        num=self.x3-self.x0
        x1,y1,x2,y2=x1*100/num,(num-y1)*100/num,x2*100/num,(num-y2)*100/num
        return [round(x1,1),round(y1,1),round(x2,1),round(y2,1)]
        
        