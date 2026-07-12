import numpy as np
import pygame
import sys
import pygame.surfarray
import game_data

class Graph:  # 每个图形的类
    def __init__(self, img, img_rect):
        self.img = img
        self.rect: pygame.Rect = img_rect
        self.calc_pos()
    
    def calc_pos(self):
        num = 25
        new_x = self.rect.x//num*num
        new_y = self.rect.y//num*num
        if self.rect.x - new_x > num//2:
            new_x += num
        if self.rect.y - new_y > num//2:
            new_y += num
        self.rect.x, self.rect.y = new_x, new_y
        
    def __lt__(self, other):
        return self.rect.w*self.rect.h < other.rect.w*other.rect.h

    @staticmethod
    def make_rect(w, h):  # 构造 w*h 的矩形
        return [(1 << w)-1]*h
    
    @staticmethod
    def make_circle(radius):
        surface = pygame.Surface((2*radius, 2*radius))
        pygame.draw.circle(surface, (0, 0, 1), (radius, radius), radius)
        sf_arr = pygame.surfarray.pixels2d(surface)
        ans = []
        for i in sf_arr:
            i = np.array2string(i, separator = '')[1:-1].replace('\n', '').replace(' ', '')
            ans.append(int(i, 2))
        return ans


class Board:
    def __init__(self, x, y, w, h):
        self.bg = [0]*h  # 背景矩阵
        self.w = w
        self.h = h
        self.x, self.y = x, y

    def update(self):
        self.bg = [0]*self.h

    def draw_one_line(self, a, b, len_b, x):
        bit_left = self.w - x - len_b
        if bit_left >= 0:
            b <<= bit_left
            b &= ((1 << self.w) - 1)
        else:
            b >>= abs(bit_left)
        return a ^ b

    def draw_one_graph(self, graph):
        x, y = graph.rect.x, graph.rect.y
        for i, num in enumerate(graph.img):
            if y+i >= self.h:
                break
            if y+i < 0:
                continue
            self.bg[y+i] = self.draw_one_line(self.bg[y+i], num, graph.rect.width, x)

    def render_to_screen(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x-1, self.y-1, self.w+2, self.h+2), width=1)
        for i in np.arange(1, self.w//25):
            for j in np.arange(1, self.h//25):
                pygame.draw.rect(screen, (120, 120, 120), (self.x+25*i-2, self.y+25*j-2, 4, 4))
        sf = pygame.surfarray.pixels3d(screen)
        fan_wei = np.arange(self.x, self.x+self.w)
        for i, num in enumerate(self.bg):
            bin_repr = np.binary_repr(num, width=self.w)  # 转成二进制类型的字符串
            arr = np.fromstring(bin_repr, dtype='int8') == 49
            sf[fan_wei[arr], self.y+i, :] = 0
    
    def is_win(self, ans):
        s, e = 0, self.h
        while(not self.bg[s]):
            s+=1
        while(not self.bg[e-1]):
            e-=1
        if e-s != len(ans):
            return False
        if self.bg[s] % ans[0]:
            return False
        nnum = self.bg[s] // ans[0]
        for i, num in enumerate(ans):
            if not(self.bg[s+i] % num == 0 and self.bg[s+i] // num == nnum):
                return False
        return True


class main:
    def __init__(self, level):
        self.board = Board(30, 290, 400, 400)
        self.ans = Board(105, 30, 250, 250)
        self.graphs = []
        self.ans_graphs = []
        for i, pos in game_data.level[level]['Graphs']:
            if i == 'Rect':
                self.graphs.append(Graph(Graph.make_rect(pos[2], pos[3]), pygame.Rect(pos[0], pos[1], pos[2], pos[3])))
            elif i == 'Circle':
                self.graphs.append(Graph(Graph.make_circle(pos[2]), pygame.Rect(pos[0], pos[1], pos[2]*2, pos[2]*2)))
        for i, pos in game_data.level[level]['Ans']:
            if i == 'Rect':
                self.ans_graphs.append(Graph(Graph.make_rect(pos[2], pos[3]), pygame.Rect(pos[0], pos[1], pos[2], pos[3])))
            elif i == 'Circle':
                self.ans_graphs.append(Graph(Graph.make_circle(pos[2]), pygame.Rect(pos[0], pos[1], pos[2]*2, pos[2]*2)))
            self.ans.draw_one_graph(self.ans_graphs[-1])
        # print(self.ans.bg)
        self.graphs.sort()
        self.active_graph = None  # 当前正在拖动的图形

    def display(self, screen, pygame_events, mouse_x, mouse_y, mouse_pressed):
        for event in pygame_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for graph in self.graphs:
                    if graph.rect.collidepoint((mouse_x-self.board.x, mouse_y-self.board.y)):
                        self.active_graph = graph
                        break
            if event.type == pygame.MOUSEMOTION:
                if self.active_graph is not None:
                    self.active_graph.rect.move_ip(event.rel)
            if event.type == pygame.MOUSEBUTTONUP:
                if self.active_graph is not None:
                    self.active_graph.calc_pos()
                self.active_graph = None
        self.board.update()
        for graph in self.graphs:
            self.board.draw_one_graph(graph)
        self.board.render_to_screen(screen)
        if self.board.is_win(self.ans.bg):
            print('答案正确')
        self.ans.render_to_screen(screen)
