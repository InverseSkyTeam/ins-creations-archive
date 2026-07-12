import pygame
import sys
from Effect import Effect

pygame.init()

# 屏幕设置
w, h = 900, 900
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('图像效果调节器')

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)
BLUE = (0, 120, 215)
DARK_BLUE = (0, 90, 160)
RED = (255, 0, 0)

# 字体设置
font = pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 24)
small_font = pygame.font.SysFont(['kaiti', 'harmonyossanssc'], 20)

USE_CACHE = True

clock = pygame.time.Clock()

class Sprite:
    def __init__(self, path):
        self.img = pygame.image.load(path).convert_alpha()
        self.mosaic = 0
        self.pixelate = 0
        self.whirl = 0
        self.fisheye = 0
        self.color = 0
        
        self.temp_image = self.img.copy()
        self.temp_color = self.temp_image.copy()
    
    def modify(self, mosaic, pixelate, whirl, fisheye, color):
        if not USE_CACHE:
            self.mosaic = mosaic
            self.pixelate = pixelate
            self.whirl = whirl
            self.fisheye = fisheye
            self.color = color
            self.temp_image = Effect.transform_image(self.img, self.mosaic, self.pixelate, self.whirl, self.fisheye)
            self.temp_color = Effect.transform_color(self.temp_image, self.color)
            return
        if self.mosaic != mosaic or self.pixelate != pixelate or self.whirl != whirl or self.fisheye != fisheye:
            self.mosaic = mosaic
            self.pixelate = pixelate
            self.whirl = whirl
            self.fisheye = fisheye
            self.temp_image = Effect.transform_image(self.img, self.mosaic, self.pixelate, self.whirl, self.fisheye)
            if self.color != color:
                self.color = color
            self.temp_color = Effect.transform_color(self.temp_image, self.color)
            return
        if self.color != color:
            self.color = color
            self.temp_color = Effect.transform_color(self.temp_image, self.color)
    
    def render(self, screen, rect):
        screen.blit(self.temp_color, self.temp_color.get_rect(center=rect.center))

class InputBox:
    def __init__(self, x, y, w, h, label, initial_value=0):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label
        self.text = str(initial_value)
        self.active = False
        self.color = GRAY
        self.label_surf = font.render(label, True, BLACK)
        self.error = False
        self.cursor_visible = False
        self.cursor_timer = 0
    
    def handle_event(self, event, keyboard):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.activate(keyboard)
            elif not keyboard.bg_rect.collidepoint(event.pos):
                self.deactivate()
        
        if self.active and event.type == pygame.KEYDOWN:
            self.process_key_event(event)
    
    def activate(self, keyboard):
        self.active = True
        self.color = BLUE
        self.cursor_visible = True
        self.cursor_timer = pygame.time.get_ticks()
        keyboard.visible = True
        keyboard.active_input = self
    
    def deactivate(self):
        self.active = False
        self.color = GRAY
    
    def process_key_event(self, event):
        if event.key == pygame.K_RETURN:
            self.deactivate()
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif event.unicode in '0123456789-.':
            test_text = self.text + event.unicode
            try:
                test_text in '-.' or float(test_text)
                self.text = test_text
                self.error = False
            except ValueError:
                self.error = True
    
    def update(self):
        if self.active:
            now = pygame.time.get_ticks()
            if now - self.cursor_timer > 500:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = now
    
    def draw(self, screen):
        screen.blit(self.label_surf, (self.rect.x, self.rect.y - 30))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.draw.rect(screen, WHITE, (self.rect.x+2, self.rect.y+2, self.rect.w-4, self.rect.h-4))
        
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        
        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + 5 + text_surface.get_width()
            pygame.draw.line(screen, BLACK, (cursor_x, self.rect.y+5), 
                           (cursor_x, self.rect.y+self.rect.h-5), 2)
        
        if self.error:
            pygame.draw.rect(screen, RED, self.rect, 2)
    
    def get_value(self):
        try:
            return float(self.text)
        except ValueError:
            return 0

class VirtualKeyboard:
    def __init__(self):
        self.visible = False
        self.keys = [
            ['7', '8', '9', '←'],
            ['4', '5', '6', '←'],
            ['1', '2', '3', '←'],
            ['0', '-', '.', '←']
        ]
        self.key_rects = []
        self.active_input = None
        self.width = 400  # 加宽以适应退格键列
        self.height = 300
        self.x = w // 2 - self.width // 2
        self.y = h - self.height - 20
        self.bg_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        key_width = 80
        key_height = 60
        margin = 10
        
        # 创建按键矩形，最后一列为退格键
        for row in range(len(self.keys)):
            for col in range(len(self.keys[row])):
                x = self.x + margin + col * (key_width + margin)
                y = self.y + margin + row * (key_height + margin)
                self.key_rects.append(pygame.Rect(x, y, key_width, key_height))
    
    def handle_event(self, event):
        if not self.visible:
            return
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.bg_rect.collidepoint(event.pos):
                self.visible = False
                if self.active_input:
                    self.active_input.deactivate()
                return
            
            for i, rect in enumerate(self.key_rects):
                if rect.collidepoint(event.pos):
                    row = i // 4  # 现在每行有4列
                    col = i % 4
                    char = self.keys[row][col]
                    
                    if self.active_input:
                        if char == '←':  # 退格键处理
                            key_event = pygame.event.Event(
                                pygame.KEYDOWN,
                                {'key': pygame.K_BACKSPACE, 'unicode': '', 'mod': 0}
                            )
                        else:
                            key_event = pygame.event.Event(
                                pygame.KEYDOWN,
                                {'unicode': char, 'key': pygame.K_UNKNOWN, 'mod': 0}
                            )
                        self.active_input.process_key_event(key_event)
    
    def draw(self, screen):
        if not self.visible:
            return
        
        pygame.draw.rect(screen, LIGHT_GRAY, self.bg_rect)
        pygame.draw.rect(screen, BLACK, self.bg_rect, 2)
        
        for i, rect in enumerate(self.key_rects):
            color = DARK_BLUE if rect.collidepoint(pygame.mouse.get_pos()) else WHITE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            
            row = i // 4
            col = i % 4
            char = self.keys[row][col]
            
            # 退格键特殊样式
            if char == '←':
                text_surface = font.render(char, True, RED)  # 退格键用红色
                # 绘制退格键图标
                pygame.draw.rect(screen, (255, 200, 200) if rect.collidepoint(pygame.mouse.get_pos()) else (255, 230, 230), rect)
            else:
                text_surface = font.render(char, True, BLACK)
            
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

# 初始化
sprite = Sprite('可多1.png')
keyboard = VirtualKeyboard()
input_boxes = [
    InputBox(50, 400, 120, 32, "马赛克", sprite.mosaic),
    InputBox(50, 480, 120, 32, "像素化", sprite.pixelate),
    InputBox(50, 560, 120, 32, "漩涡", sprite.whirl),
    InputBox(50, 640, 120, 32, "鱼眼", sprite.fisheye),
    InputBox(50, 720, 120, 32, "颜色", sprite.color)
]

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        keyboard.handle_event(event)
        
        for box in input_boxes:
            box.handle_event(event, keyboard)
    for box in input_boxes:
        box.update()
    
    values = [box.get_value() for box in input_boxes]
    sprite.modify(*values)
    
    screen.fill(WHITE)
    # pygame.draw.rect(screen, 'red', (0, 0, w, h))
    sprite.render(screen, pygame.Rect(50, 50, 300, 300))
    
    for box in input_boxes:
        box.draw(screen)
    
    keyboard.draw(screen)
    
    # instructions = small_font.render("点击输入框可调出虚拟键盘，点击键盘外部可关闭", True, BLACK)
    # screen.blit(instructions, (50, 780))
    fps = small_font.render(f"FPS: {round(clock.get_fps(), 3)}", True, BLACK)
    screen.blit(fps, (10, 10))
    
    pygame.display.update()
    clock.tick(114514)