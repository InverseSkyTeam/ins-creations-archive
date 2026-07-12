import copy
import numpy as np
import pygame

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
colors = {}
with open('colors.txt') as file:
    for line in file:
        bg, col_str = line.rstrip('\n').split(maxsplit=1, sep=' ')
        colors[int(col_str)] = bg
robot_img = pygame.image.load('robot.png')


class Maze:
    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            res = f.read().split('\n')
        self.H, self.W = res[0].split(' ')
        self.H, self.W = int(self.H), int(self.W)
        self.mp_data = [[0 for _ in range(20)] for _ in range(20)]
        for i in range(self.H+2):
            for j in range(self.W+2):
                self.mp_data[i][j] = -2
        for i in range(1, self.H+1):
            temp = res[i].split(' ')
            for j in range(1, self.W+1):
                self.mp_data[i][j] = -int(temp[j-1])
        self.mp = copy.deepcopy(self.mp_data)
        self.mp_run = copy.deepcopy(self.mp_data)

    def check(self, x, y):
        return 1<=x and x<=self.H and 1<=y and y<=self.W and self.mp[x][y]>=0

    def run(self, command):
        self.mp_run = copy.deepcopy(self.mp_data)
        mx, tp = command.mx, command.tp.copy()
        lim = 0
        X = Y = 1
        while lim<=500000:  # 步数限制在500000
            lim += 1
            nex = tp[self.mp_run[X][Y]+2][self.mp_run[X][Y-1]+2][self.mp_run[X+1][Y]+2][self.mp_run[X][Y+1]+2][self.mp_run[X-1][Y]+2]
            self.mp_run[X][Y]=nex[0]  # 设置颜色
            # print([self.mp_run[X][Y]+2],[self.mp_run[X][Y-1]+2],[self.mp_run[X+1][Y]+2],[self.mp_run[X][Y+1]+2],[self.mp_run[X-1][Y]+2])
            if chr(nex[1])=='H':
                continue
            elif chr(nex[1])=='W':
                Y -= 1
                if self.mp_run[X][Y]<0:
                    return "Invalid move"
            elif chr(nex[1])=='S':
                X += 1
                if self.mp_run[X][Y]<0:
                    return "Invalid move"
            elif chr(nex[1])=='E':
                Y += 1
                if self.mp_run[X][Y]<0:
                    return "Invalid move"
            elif chr(nex[1])=='N':
                X -= 1
                if self.mp_run[X][Y]<0:
                    return "Invalid move"
            else:
                break
            yield lim, X, Y
        if lim>500000:
            return "Too many steps"
    
    def render(self, screen, rect, X, Y):
        gezi_size = min(rect.w, rect.h)//max(self.W, self.H)
        x, y = rect.x + (rect.w - self.W * gezi_size) // 2, rect.y + (rect.h - self.H * gezi_size) // 2
        font = pygame.font.SysFont('arial', gezi_size//2)
        for i in range(1, self.H+1):
            x = rect.x + (rect.w - self.W * gezi_size) // 2
            for j in range(1, self.W+1):
                temp_rect = pygame.Rect(x, y, gezi_size, gezi_size)
                pygame.draw.rect(screen, colors[self.mp_run[i][j]], temp_rect)
                if self.mp_run[i][j] == -1:
                    tl = list(temp_rect.topleft)
                    tr = list(temp_rect.topright)
                    br = list(temp_rect.bottomright)
                    bl = list(temp_rect.bottomleft)
                    tr[0]-=2
                    br[0]-=2
                    br[1]-=2
                    bl[1]-=2
                    pygame.draw.line(screen, (255, 0, 0), tl, br, width=2)
                    pygame.draw.line(screen, (255, 0, 0), tr, bl, width=2)
                else:
                    sf_tmp = font.render(str(self.mp_run[i][j]), True, (0,)*3)
                    screen.blit(sf_tmp, sf_tmp.get_rect(center=temp_rect.center))
                pygame.draw.rect(screen, (0, 0, 0), temp_rect, width=1)
                if i==X and j==Y:
                    _sf = pygame.transform.smoothscale(robot_img, (gezi_size//1.3, gezi_size//1.3))
                    screen.blit(_sf, _sf.get_rect(center=temp_rect.center))
                x += gezi_size
            y += gezi_size

    def evaluating(self, command):
        self.mp = copy.deepcopy(self.mp_data)
        mx, tp = command.mx, command.tp.copy()
        lim = col = _sum = 0
        que = [[0, 0] for _ in range(410)]  # 用于bfs的队列
        X = Y = 1
        mx = 0
        while lim <= 500000:  # 步数限制在500000
            lim += 1
            nex = tp[self.mp[X][Y]+2][self.mp[X][Y-1]+2][self.mp[X+1][Y]+2][self.mp[X][Y+1]+2][self.mp[X-1][Y]+2]
            self.mp[X][Y] = nex[0]  # 设置颜色
            mx = max(mx, nex[0])
            # print([self.mp[X][Y]+2],[self.mp[X][Y-1]+2],[self.mp[X+1][Y]+2],[self.mp[X][Y+1]+2],[self.mp[X-1][Y]+2])
            if chr(nex[1]) == 'H':
                continue
            elif chr(nex[1]) == 'W':
                Y -= 1
                if self.mp[X][Y]<0:
                    return "Invalid move"
            elif chr(nex[1]) == 'S':
                X += 1
                if self.mp[X][Y]<0:
                    return "Invalid move"
            elif chr(nex[1]) == 'E':
                Y += 1
                if self.mp[X][Y]<0:
                    return "Invalid move"
            elif chr(nex[1]) == 'N':
                X -= 1
                if self.mp[X][Y]<0:
                    return "Invalid move"
            else:
                break
        if lim > 500000:
            return "Too many steps"
        dp = [[0x3F3F3F3F for _ in range(20)] for _ in range(20)]
        dp[1][1] = 1
        st = ed = 1
        que[st] = [1, 1]
        while st <= ed:  # BFS求最短路
            pos = que[st]
            st += 1
            for k in range(4):
                tx = pos[0] + dx[k]
                ty = pos[1] + dy[k]
                if not self.check(tx,ty):  # 到达边界
                    continue
                if dp[tx][ty] > dp[pos[0]][pos[1]]+1:
                    dp[tx][ty] = dp[pos[0]][pos[1]]+1
                    ed += 1
                    que[ed] = [tx, ty]
        for i in range(1, self.H+1):
            for j in range(1, self.W+1):
                col = max(col, self.mp[i][j])  # 最大颜色
        for i in range(1, self.H+1):
            for j in range(1, self.W+1):
                _sum += (self.mp[i][j]==1)  # 状态为1的格子总数
        # print(dp[self.H][self.W], _sum)
        if _sum!=dp[self.H][self.W]:  # 最少步数不等于1的数量（不是最短路）
            return "Output isn't correct"
        if self.mp[1][1] != 1 or self.mp[self.H][self.W] != 1:  # 起始位置和结束位置不是1
            return "Output isn't correct"
        st = ed = 1
        que[st] = [1, 1]
        dis = [[0x3F3F3F3F for _ in range(20)] for _ in range(20)]
        dis[1][1] = 1
        while st <= ed:  # 沿着机器人的路径再一次bfs，判断路径是否连通
            pos = que[st]
            st += 1
            for k in range(4):
                tx = pos[0] + dx[k]
                ty = pos[1] + dy[k]
                if not self.check(tx,ty):
                    continue
                if self.mp[tx][ty] != 1:
                    continue
                if dis[tx][ty] > dis[pos[0]][pos[1]]+1:
                    dis[tx][ty] = dis[pos[0]][pos[1]]+1
                    ed += 1
                    que[ed] = [tx,ty]
        # print(dis[self.H][self.W], dp[self.H][self.W])
        if dis[self.H][self.W] != dp[self.H][self.W]:
            return "Output isn't correct"
        score = (col <= 1)  # 最大颜色是否是1
        if mx <= 11:
            score += 1
        if mx <= 10:
            score += 1
        if mx <= 9:
            score += 1
        if mx <= 8:
            score += 1
        if mx <= 7:
            score += 1
        if mx <= 6:
            score += 1
        if score < 7:
            return "PC（部分正确）"
        else:
            return "AC"


class Command:
    def __init__(self):
        self.command = []
        self.tp = np.zeros([22, 22, 22, 22, 22, 2], dtype=int)  # python开数组太慢，用np数组加速
        self.mx = 0

    def load_file(self, name):
        with open(name, 'r') as f:
            _temp = f.read().split('\n')
        self.command.clear()
        for i, c in enumerate(_temp):
            c_ = c.split(' ')
            for j in range(len(c_)-1):
                c_[j] = int(c_[j])
            self.command.append(c_)
    
    def parse_command(self):
        self.tp = np.zeros([22, 22, 22, 22, 22, 2], dtype=int)
        self.mx = 0
        for i, temp in enumerate(self.command):
            a, b, c, d, e, Z, A = temp
            if a < -2 or a > 19:
                return "Invalid array"
            if b < -2 or b > 19:
                return "Invalid array"
            if c < -2 or c > 19:
                return "Invalid array"
            if d < -2 or d > 19:
                return "Invalid array"
            if e < -2 or e > 19:
                return "Invalid array"
            if Z < 0 or Z > 19:
                return "Invalid color"
            a += 2
            b += 2
            c += 2
            d += 2
            e += 2
            if A != 'H' and A != 'W' and A != 'S' and A != 'E' and A != 'N' and A != 'T':
                return "Invalid action"
            if self.tp[a][b][c][d][e][1]:  # 有相同的指令
                return "Same state array"
            self.tp[a][b][c][d][e][0] = Z  # 存储指令
            self.tp[a][b][c][d][e][1] = ord(A)
            self.mx = max(self.mx, Z)  # 记录最大的Z，用于判分
        return 'OK'


tests = []
for i in range(20):
    maze = Maze(f'test/robot{i+1}.txt')
    tests.append(maze)
