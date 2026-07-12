import pygame
import sys


# 初始化 Pygame
pygame.init()
pygame.mixer.init()

# 颜色定义
# BACKGROUND = (255, 255, 255)
# UI_BACKGROUND = (242, 242, 242)
# PROGRESS_BG = (189, 203, 225)
# PROGRESS_FG = (84, 143, 255)
# PROGRESS_HEAD = (255, 255, 255)
# TEXT_COLOR = (23, 23, 23)

# 颜色定义
BACKGROUND = (255, 255, 255)
UI_BACKGROUND = (255, 240, 240)  # 浅红色背景
PROGRESS_BG = (255, 200, 200)    # 浅红色进度条背景
PROGRESS_FG = (220, 0, 0)        # 深红色进度条前景
PROGRESS_HEAD = (255, 255, 255)  # 白色进度条头部
TEXT_COLOR = (100, 0, 0)         # 深红色文字

FONT_NAMES = [
    "notosanscjktcregular",
    "notosansmonocjktcregular",
    "notosansregular",
    "microsoftjhenghei",
    "microsoftyahei",
    "msgothic",
    "msmincho",
    "unifont",
    "Arial",
]

# 窗口设置
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame 音频播放器 - 支持进度调整")


class Player:
    def __init__(self):
        self.is_pause = False
        self.length_seconds = None
        self.offset = 0
        
        self.last_pos = -1
    
    @property
    def is_play(self):
        return not (pygame.mixer.music.get_pos() == -1)
    
    def load(self, path):
        pygame.mixer.music.load(path)
        self.offset = 0
        self.length_seconds = 573.2742309570312  # pygame.mixer.Sound(path).get_length()
    
    def play(self):
        self.is_pause = False
        self.offset = 0
        pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
    
    def stop(self):
        self.is_pause = False
        self.offset = 0
        pygame.mixer.music.stop()
    
    def set_pos(self, seconds):
        if not self.is_play:
            self.play()
        self.offset += int((seconds - self.get_pos()) * 1000)
        pygame.mixer.music.set_pos(seconds)
    
    def get_pos(self):
        res = pygame.mixer.music.get_pos()
        if res == -1:
            self.last_pos = -1
            return 0
        if res < self.last_pos:
            # print(114514)
            return (self.offset + self.last_pos) / 1000
        # print(1919)
        self.last_pos = res
        return (self.offset + res) / 1000
    
    def get_state(self):
        if not self.is_play:
            return False
        return not self.is_pause
    
    def pause(self):  # 暂停
        self.is_pause = True
        pygame.mixer.music.pause()
    
    def unpause(self):
        self.is_pause = False
        pygame.mixer.music.unpause()


class PlayButton:
    def __init__(self, player: Player, rect: pygame.Rect):
        self.play_image = pygame.image.load('play.png').convert_alpha()
        self.pause_image = pygame.image.load('pause.png').convert_alpha()
        self.player = player
        self.rect = rect
    
    def draw(self, surface):
        image = self.pause_image if self.player.get_state() else self.play_image
        image = pygame.transform.smoothscale(image, self.rect.size)
        surface.blit(image, self.rect)
    
    def handle_event(self, _event):
        if _event.type == pygame.MOUSEBUTTONDOWN and _event.button == 1 and self.rect.collidepoint(_event.pos):
            if not self.player.is_play:
                self.player.play()
            elif self.player.is_pause:
                self.player.unpause()
            else:
                self.player.pause()


class ProgressBar:
    def __init__(self, player: Player, rect: pygame.Rect):
        self.player = player
        self.rect = rect
        self.line_rect = pygame.Rect(self.rect.x, 0, self.rect.w, self.rect.h // 15)
        self.line_rect.centery = self.rect.centery
        self.font_size = self.rect.h // 5
        self.font = pygame.font.SysFont(FONT_NAMES, self.font_size)
        
        self.dragging = False
        self.temp_progress = None
    
    @property
    def progress(self):
        if self.dragging and self.temp_progress is not None:
            return self.temp_progress
        return self.player.get_pos() / self.player.length_seconds
    
    @property
    def progress_seconds(self):
        if self.dragging and self.temp_progress is not None:
            return int(self.temp_progress * self.player.length_seconds)
        return self.player.get_pos()
    
    @staticmethod
    def time_convert(seconds):
        seconds = int(seconds)
        return f'{seconds // 60:02d}:{seconds % 60:02d}'
    
    def draw(self, surface):
        border = self.line_rect.h // 2
        head_raidus = int(self.rect.h * 0.15)
        head_x = self.line_rect.x + int((self.line_rect.w - head_raidus * 2) * self.progress) + head_raidus
        line_fg_rect = self.line_rect.copy()
        line_fg_rect.w = max(head_x - self.line_rect.x, self.line_rect.h)
        pygame.draw.rect(surface, PROGRESS_BG, self.line_rect, border_radius=border)
        pygame.draw.rect(surface, PROGRESS_FG, line_fg_rect, border_radius=border)
        pygame.draw.circle(surface, PROGRESS_HEAD, (head_x, line_fg_rect.centery), head_raidus)
        
        # progress = (head_x - self.rect.x - int(self.rect.h * 0.15)) / (self.rect.w - int(self.rect.h * 0.3))
        left_text = self.font.render(self.time_convert(self.progress_seconds), True, TEXT_COLOR)
        right_text = self.font.render(self.time_convert(self.player.length_seconds), True, TEXT_COLOR)
        text_y = self.line_rect.bottom + (self.rect.bottom - self.line_rect.bottom - self.font_size) // 2
        surface.blit(left_text, (self.line_rect.left, text_y))
        surface.blit(right_text, (self.line_rect.right - right_text.get_width(), text_y))
    
    def get_mouse_progress(self, x):
        offset_x = x - self.rect.x - self.rect.h * 0.15
        progress = offset_x / (self.rect.w - self.rect.h * 0.3)
        return max(0.0, min(1.0, progress))
    
    def handle_event(self, _event):
        rect = pygame.Rect(self.rect.x, 0, self.rect.w, int(self.rect.h * 0.3))
        rect.centery = self.rect.centery
        if _event.type == pygame.MOUSEBUTTONDOWN and _event.button == 1 and rect.collidepoint(_event.pos):
            self.dragging = True
            self.temp_progress = self.player.get_pos() / self.player.length_seconds
        elif _event.type == pygame.MOUSEMOTION:
            self.temp_progress = self.get_mouse_progress(_event.pos[0])
        elif _event.type == pygame.MOUSEBUTTONUP and _event.button == 1 and self.dragging:
            progress = self.get_mouse_progress(_event.pos[0])
            self.player.set_pos(progress * self.player.length_seconds)
            self.temp_progress = None
            self.dragging = False

    
class UI:
    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        self.player = Player()
        
        button_size = self.rect.h // 2
        padding = int(button_size * 0.7)
        
        button_rect = pygame.Rect(self.rect.x + padding, 0, button_size, button_size)
        button_rect.centery = self.rect.centery
        self.play_button = PlayButton(self.player, button_rect)
        
        progress_rect = pygame.Rect(button_rect.right + padding, self.rect.y, 0, self.rect.h)
        progress_rect.w = self.rect.right - int(padding * 1.2) - progress_rect.x
        self.progress_bar = ProgressBar(self.player, progress_rect)
    
    def load(self, path):
        self.player.load(path)
    
    def draw(self, surface):
        pygame.draw.rect(surface, UI_BACKGROUND, self.rect, border_radius=self.rect.h//3)
        self.play_button.draw(surface)
        self.progress_bar.draw(surface)
    
    def handle_event(self, events):
        for _event in events:
            self.play_button.handle_event(_event)
            self.progress_bar.handle_event(_event)


class BackGround:
    def __init__(self):
        self.image = pygame.transform.smoothscale(pygame.image.load('background.png'), (WIDTH, HEIGHT)).convert_alpha()
    
    def draw(self, _screen):
        _screen.blit(self.image, (0, 0))


background = BackGround()
ui = UI(pygame.Rect((WIDTH - 800) // 2, (HEIGHT - 160) // 2, 800, 160))
ui.load('国际歌.ogg')

# 主循环
clock = pygame.time.Clock()
while True:
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ui.handle_event(pygame_events)

    # 绘制界面
    screen.fill(BACKGROUND)
    background.draw(screen)
    # pygame.draw.rect(screen, (0,0,0), (0,0,WIDTH, HEIGHT), 1)
    ui.draw(screen)

    pygame.display.flip()
    clock.tick(60)