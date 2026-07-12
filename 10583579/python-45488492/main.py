import pygame
import numpy as np

class Wer:
    def __init__(self, x, y, z):
        self.x = np.array(x)
        self.y = np.array(y)
        self.z = np.array(z)
        self.scx = 0
        self.scy = 0
        self.scz = 0
        self.dl = []

    def rotate(self, angle_x, angle_y):
        x = self.x
        y = self.y
        self.y = y * np.cos(angle_x) - self.z * np.sin(angle_x)
        self.z = y * np.sin(angle_x) + self.z * np.cos(angle_x)
        self.x = x * np.cos(angle_y) + self.z * np.sin(angle_y)
        self.z = self.z * np.cos(angle_y) - x * np.sin(angle_y)

    def translate(self, x, y, z):
        self.x = self.x - x
        self.y = self.y - y
        self.z = self.z - z

    def transform(self, pxa, pya):
        self.scy = self.y * np.cos(pxa) - self.z * np.sin(pxa)
        self.z = self.y * np.sin(pxa) + self.z * np.cos(pxa)
        self.scx = self.x * np.cos(pya) + self.z * np.sin(pya)
        self.scz = self.z * np.cos(pya) - self.x * np.sin(pya)

    def perspective(self, w, scx, scy):
        dx = self.scx / self.scz * w + scx
        dy = self.scy / self.scz * w + scy
        self.dl = [[dx[i], dy[i]] for i in range(len(dx))]
        return self.dl


class Polygon(Wer):
    def __init__(self, screen, x, y, z, color, w):
        super().__init__(x, y, z)
        self.color = color
        self.w = w
        self.screen = screen

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, self.dl, self.w)


class Cube(Wer):
    def __init__(self, screen, xl, yl, zl, rgb, w):
        x = [xl, -xl, -xl, xl, xl, -xl, -xl, xl]
        y = [yl, yl, -yl, -yl, yl, yl, -yl, -yl]
        z = [zl, zl, zl, zl, -zl, -zl, -zl, -zl]
        super().__init__(x, y, z)
        self.color = rgb
        self.w = w
        self.screen = screen
        self.opacity = [1] * 6

    def draw(self):
        polygons, heights = [], []
        for i in range(2):
            polygons.append(self.dl[i * 4:i * 4 + 4])
            polygons.append(self.dl[i * 2:i * 2 + 2] + [self.dl[i * 2 + 5]] + [self.dl[i * 2 + 4]])
            polygons.append([self.dl[4 - i * 2]] + [self.dl[i * 6]] + [self.dl[3 + i * 2]] + [self.dl[(7 + i * 2) % 8]])
            heights.append(self.scz[i * 4:i * 4 + 4])
            heights.append(list(self.scz[i * 2:i * 2 + 2]) + [self.scz[i * 2 + 5]] + [self.scz[i * 2 + 4]])
            heights.append([self.scz[4 - i * 2]] + [self.scz[i * 6]] + [self.scz[3 + i * 2]] + [self.scz[(7 + i * 2) % 8]])
        for i in range(6):
            max_height, selected_poly = 0, 0
            for j in range(len(polygons)):
                height = max([heights[j][k] for k in range(4)])
                if height > max_height:
                    max_height = height
                    selected_poly = j
            if len(polygons) == 0:  # 添加判断，避免索引越界错误
                break
            pygame.draw.polygon(self.screen, np.array(self.color[selected_poly]) * self.opacity[selected_poly], polygons[selected_poly], self.w)
            polygons.pop(selected_poly)
            self.color.pop(selected_poly)
            heights.pop(selected_poly)


pygame.init()
screen = pygame.display.set_mode((800, 800))

dlx = [500, 500, -500, -500, -500, -500, 500, 500, 500, 500, 500, -500, -500, -500, -500, 500]
dly = [-500, 500, -500, 500, -500, 500, -500, 500, -500, 500, 500, 500, 500, -500, -500, -500]
dlz = [500, 500, 500, 500, -500, -500, -500, -500, 500, 500, 500, 500, -500, -500, -500, 500]

def draw_3d(screen, dlx, dly, dlz, xa, ya, pxa, pya):
    cube_obj = Cube(screen, 500, 500, 500, [(i, i, i) for i in range(64, 256, 32)], 0)
    cube_obj.rotate(xa, ya)
    cube_obj.translate(0, 0, -5000)
    cube_obj.transform(1/8,1/8)
    cube_obj.perspective(1000, 400, 400)
    cube_obj.draw()


xu = 0
yu = 0

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    xu += 0.01
    yu += 0.01
    draw_3d(screen, dlx, dly, dlz, yu, xu,0,0)
    pygame.display.update()
    clock.tick(60)
