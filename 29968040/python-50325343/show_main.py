import pygame
import os
import re
import random
import datetime
import threading as thr
import math
import hashlib
import webbrowser as wb
import cProfile
from PIL import Image, ImageFilter
from PgMarkdown import PygameMarkdown, Load


md = PygameMarkdown.MarkdownRenderer()


def calc_colors(opaque_color, transparent_color):
    opaque_r, opaque_g, opaque_b = opaque_color
    alpha = transparent_color[3]
    result_r = ((1 - alpha) * opaque_r + alpha * transparent_color[0])
    result_g = ((1 - alpha) * opaque_g + alpha * transparent_color[1])
    result_b = ((1 - alpha) * opaque_b + alpha * transparent_color[2])

    return int(result_r), int(result_g), int(result_b)


def calc_rect_center(img, x, y, w, h):
    img_w, img_h = img.get_size()
    return pygame.Rect(x + (w-img_w)//2, y + (h-img_h)//2, img_w, img_h)


def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    md5_value = md5_hash.hexdigest()
    return md5_value[:14]


class Blog:
    def __init__(self, w, h, bg_color):
        self.w = w
        self.h = h
        self.bg_color = bg_color
        self.logo = pygame.font.SysFont('SimHei', 18).render('吴宇航的博客', True, (76, 73, 72))
        self.logo_rect = calc_rect_center(self.logo, 0, 0, self.w, 60)
        self.follow_rect = None
        self.avatar = pygame.transform.smoothscale(pygame.image.load('avatar.png'), (128, 128))
        self.pos = pygame.image.load('pos.png')
        self.title_bg = pygame.Surface((w, 64+50), pygame.SRCALPHA).convert_alpha()
        self.yzx_shadow = self.create_shadow(pygame.Rect(21, 102, 250, 303)).convert_alpha()
        self.init_title_bg()
        self.data = Data(pygame.Rect(292, 102, self.w - 313, self.h - 60 - 2*42))
        self.font_21 = pygame.font.SysFont('SimHei', 21)
        self.font_14 = pygame.font.SysFont('SimHei', 14)

    @staticmethod
    def blue_img(sf, radius):
        pygame.image.save(sf, 'tmp.png')
        pil_image = Image.open('tmp.png')
        img1 = pil_image.filter(ImageFilter.GaussianBlur(radius=radius))
        res = pygame.image.fromstring(img1.tobytes(), img1.size, img1.mode)
        return res

    def render_text(self, screen, pos, txt, font_size, font_color, center_x=False, center_y=False):
        font = self.font_21 if font_size == 21 else self.font_14
        sf = font.render(txt, True, font_color)
        new_x = pos.x+(pos.width-sf.get_width())//2 if center_x else pos.x
        new_y = pos.y+(pos.height-sf.get_height())//2 if center_y else pos.y
        screen.blit(sf, (new_x, new_y))

    def init_title_bg(self):
        pygame.draw.rect(self.title_bg, (0, 0, 0, int(255*0.05)), (0, 4, self.w, 60))
        self.title_bg = self.blue_img(self.title_bg, 10)
        pygame.draw.rect(self.title_bg, (255, 255, 255), (0, 0, self.w, 60))
        self.title_bg.blit(self.logo, self.logo_rect)

    @staticmethod
    def create_shadow(rect):
        w, h = rect.w, rect.h
        sf = pygame.Surface((w + 50, h + 50), pygame.SRCALPHA)
        pygame.draw.rect(sf, (0, 0, 0, int(255*0.05)), (25, 29, w, h), border_radius=4)
        sf = Blog.blue_img(sf, 10)
        return sf

    def render_yzx(self, screen, mouse_pos, w):
        screen.blit(self.yzx_shadow, (21 - 25, 102 - 25))
        pygame.draw.rect(screen, (255, 255, 255), (21, 102, w, 303), border_radius=4)
        screen.blit(self.avatar, calc_rect_center(self.avatar, 21, 123, w, self.avatar.get_height()))
        self.render_text(screen, pygame.Rect(21, 135 + self.avatar.get_height(), w, 0),
                         '吴宇航', 21, (54,)*3, True)
        self.render_text(screen, pygame.Rect(21, 164 + self.avatar.get_height(), w, 0),
                         '个人博客', 14, (74,) * 3, True)
        self.follow_rect = pygame.Rect(42, 208 + self.avatar.get_height() + self.pos.get_height(), w - 42, 32)
        if self.follow_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (39, 108, 218), self.follow_rect, border_radius=114514)
        else:
            pygame.draw.rect(screen, (50, 115, 220), self.follow_rect, border_radius=114514)
        self.render_text(screen, self.follow_rect, '关注我', 14, (255,) * 3, True, True)
        return self.follow_rect.bottom + 42

    def render(self, screen, mouse_pos, mouse_pressed, pygame_events):
        screen.blit(self.title_bg, (0, 0))
        self.render_yzx(screen, mouse_pos, 250)
        self.data.render(screen, mouse_pos, mouse_pressed, pygame_events)
        if mouse_pressed and self.logo_rect.collidepoint(mouse_pos):
            self.data.mode = 'home'
        for event in pygame_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.follow_rect.collidepoint(mouse_pos):
                    wb.open('https://github.com/wuyuhangxyz')


class Data:
    def __init__(self, rect):
        self.rect = rect
        self.mode = 'home'
        self.data = []
        self.load_data('./Article')
        self.page = 1
        self.font = pygame.font.SysFont('SimHei', 14)

    @staticmethod
    def my_replace(string, old, new=''):
        for i in old:
            string = string.replace(i, new)
        return string

    @staticmethod
    def lexer_code(code):
        title = re.search(r'title:\s*(.*?)\n', code).group(0)
        title = re.sub(r'title:\s*', '', title).replace('\n', '')

        date = re.search(r'date:\s*(.*?)\n', code).group(0)
        date = re.sub(r'date:\s*', '', date).replace('\n', '')

        code = re.sub(r"---(.*?)---", "", code, flags=re.DOTALL)
        code = '# ' + title + '\n\n' + re.sub(r'<\s*!--\s*more\s*--\s*>', '', code)

        return {
            'title': title,
            'date': date,
            'img': None,
            'code': code,
            'time': datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def scale_img(img, width, height):
        aspect_ratio = img.get_width() / img.get_height()
        target_ratio = width / height
        if aspect_ratio > target_ratio:
            new_height = height
            new_width = int(height * aspect_ratio) + 1
        else:
            new_width = width
            new_height = int(width / aspect_ratio) + 1
        resized_img = pygame.transform.smoothscale(img, (new_width, new_height))
        x_offset = (new_width - width) // 2
        y_offset = (new_height - height) // 2
        result_img = resized_img.subsurface((x_offset, y_offset, width, height))

        result_sf = pygame.Surface(result_img.get_size(), pygame.SRCALPHA)
        make_sf = pygame.Surface(result_img.get_size(), pygame.SRCALPHA)
        pygame.draw.rect(make_sf, (255, 255, 255, 255), pygame.Rect((0, 0), result_img.get_size()),
                         border_top_left_radius=4, border_top_right_radius=4)
        result_sf.blit(result_img, (0, 0))
        result_sf.blit(make_sf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
        return result_sf

    def get_cover(self):
        files = os.listdir('./cover')
        for i, url in enumerate(self.data):
            self.data[i]['img'] = pygame.image.load('cover/' + random.choice(files))

    def load_data(self, path):
        if path[-1] not in ['\\', '/']:
            path += '\\'
        files = os.listdir(path)
        self.data = []
        for name in files:
            if name.endswith('.md_html'):
                continue
            with open(path+name, 'r', encoding='utf-8') as f:
                code = f.read()
            self.data.append(self.lexer_code(code))
        self.data.sort(key=lambda a: a['time'], reverse=True)
        tt = thr.Thread(target=self.get_cover, args=(), name="T3")
        tt.start()

    def render_home(self, screen, mouse_pos, mouse_pressed):
        x, y = self.rect.x, self.rect.y
        for i, data in enumerate(self.data):
            if i // 4 == self.page-1 and data['img']:
                screen.blit(data['img'], (x, y))
                new_y = y + data['img'].get_height()
                pygame.draw.rect(screen, (255,) * 3, (x, new_y, data['img'].get_width(), 50),
                                 border_bottom_left_radius=4, border_bottom_right_radius=4)
                cover_rect = pygame.Rect(x, y, data['img'].get_width(), data['img'].get_height() + 50)
                screen.blit(self.font.render(data['title'], True, (54, )*3), (x+21, new_y + 18))
                if i % 2 == 0:
                    x += (self.rect.width-21)//2 + 21
                else:
                    x = self.rect.x
                    y += 250

                if mouse_pressed and cover_rect.collidepoint(mouse_pos):
                    self.mode = i
                    md.load_data(Load.load_string(data['code'], data['title']))
                    md.set_area(surface=screen, offset_x=self.rect.x, offset_y=self.rect.y,
                                width=self.rect.width, height=self.rect.height, margin=21)
        page_max = math.ceil(len(self.data)/4)
        x = self.rect.x + (self.rect.width - page_max*30 - (page_max - 1) * 10)//2
        for i in range(1, page_max+1):
            color = (50, 115, 220) if i == self.page else (255, )*3
            color_num = (255, )*3 if i == self.page else (54,) * 3
            page_rect = pygame.Rect(x, self.rect.bottom - 15, 30, 30)
            pygame.draw.rect(screen, color, page_rect, border_radius=4)
            num_sf = self.font.render(str(i), True, color_num)
            screen.blit(num_sf, (x + (30-num_sf.get_width())//2, self.rect.bottom - 15 + 8))
            x += 40
            if mouse_pressed and page_rect.collidepoint(mouse_pos):
                self.page = i

    def render(self, screen, mouse_pos, mouse_pressed, pygame_events):
        if self.mode == 'home':
            self.render_home(screen, mouse_pos, mouse_pressed)
        else:
            pygame.draw.rect(screen, (255, )*3, self.rect, border_radius=4)
            md.display(pygame_events, mouse_pos[0], mouse_pos[1], mouse_pressed)
