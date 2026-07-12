import pygame
from config import Config
from util import clamp


class BaseButton:
    def __init__(self, border_color, text, have_hover):
        self.border_color = border_color
        self.have_hover = have_hover
        self.font = pygame.font.SysFont('sans-serif', 16)
        self.text = self.font.render(text, True, (238,)*3).convert_alpha()
        self.all_down = False

    def set_mouse(self, x, y, w, h, mouse_pos):
        if pygame.Rect(x + 3, y, w - 3, h).collidepoint(mouse_pos):
            if self.have_hover:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def render_bg(self, screen, x, y, w, h, mouse_pos):
        if self.have_hover and pygame.Rect(x + 3, y, w - 3, h).collidepoint(mouse_pos):
            pygame.draw.rect(screen, (17,) * 3, (x, y, w, h))
        else:
            pygame.draw.rect(screen, (26,) * 3, (x, y, w, h))
        pygame.draw.rect(screen, self.border_color, (x, y, 3, h))
        pygame.draw.line(screen, (44,) * 3, (x + 3, y + h - 1), (x + w - 1, y + h - 1))

        text_w = int((w - 3 - 5 - 4) * 0.4)
        text_sf = pygame.Surface((text_w, h - 1), pygame.SRCALPHA)
        text_sf.blit(self.text, self.text.get_rect(midleft=(0, (h-1)//2)))
        screen.blit(text_sf, (x + 3 + 5, y))

    def render(self, *args):
        pass

    def handle_mouse_down(self, *args):
        pass


class FuncButton(BaseButton):
    def __init__(self, border_color, text, func):
        super().__init__(border_color, text, True)
        self.func = func

    def handle_mouse_down(self, mouse_pos, x, y, w, h):
        if pygame.Rect(x + 3, y, w - 3, h).collidepoint(mouse_pos):
            self.func()


class CheckBoxButton(BaseButton):
    def __init__(self, border_color, text, name):
        super().__init__(border_color, text, True)
        self.name = name
        self.img = pygame.image.load('ui.png').convert()

    def handle_mouse_down(self, mouse_pos, x, y, w, h):
        if pygame.Rect(x + 3, y, w - 3, h).collidepoint(mouse_pos):
            setattr(Config, self.name, not getattr(Config, self.name))

    def render(self, screen, x, y, w, h, mouse_pos):
        x_new = x + 3 + 5 + int((w - 3 - 5 - 4) * 0.4)
        rect = pygame.Rect(x_new + 4, y + 9, 13, 13)
        if getattr(Config, self.name):
            pygame.draw.rect(screen, (0, 117, 255), rect, border_radius=2)
            screen.blit(self.img, self.img.get_rect(center=rect.center))
        else:
            pygame.draw.rect(screen, (255,) * 3, rect, border_radius=2)
            pygame.draw.rect(screen, (118,) * 3, rect, width=1, border_radius=2)


class ScrollButton(BaseButton):
    def __init__(self, border_color, text, name, start, end):
        super().__init__(border_color, text, False)
        self.name = name
        self.start, self.end = start, end
        self.font = pygame.font.SysFont('Arial', 14)
        self.all_down = True

    def set_mouse(self, x, y, w, h, mouse_pos):
        new_w = int((w - 3 - 5 - 4) * 0.6 * 0.66)
        start_x = x + 3 + int((w - 3 - 5 - 4) * 0.4)
        rect = pygame.Rect(start_x, y + 4, new_w, 19)
        if pygame.Rect(x + 3, y, w - 3, h).collidepoint(mouse_pos):
            if rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def handle_mouse_down(self, mouse_pos, x, y, w, h):
        new_w = int((w - 3 - 5 - 4) * 0.6 * 0.66)
        start_x = x + 3 + int((w - 3 - 5 - 4) * 0.4)
        rect = pygame.Rect(start_x, y + 4, new_w, 19)
        if rect.collidepoint(mouse_pos):
            percent = (mouse_pos[0] - rect.x) / new_w
            setattr(Config, self.name, self.start + percent*(self.end-self.start))

    def render_text(self, screen, x, y, w):
        new_w = int((w - 3 - 5 - 4) * 0.6 * 0.3) + 6
        rect = pygame.Rect(x + w - new_w - 4, y + 4, new_w, 21)
        pygame.draw.rect(screen, (48,) * 3, rect)
        data = round(getattr(Config, self.name))
        text = self.font.render(str(data), True, (47, 161, 214))
        screen.blit(text, text.get_rect(midleft=(rect.x + 3, rect.centery)))

    def render_scroll(self, screen, x, y, w):
        new_w = int((w - 3 - 5 - 4) * 0.6 * 0.66)
        start_x = x + 3 + int((w - 3 - 5 - 4) * 0.4)
        rect = pygame.Rect(start_x, y + 4, new_w, 19)
        pygame.draw.rect(screen, (48,)*3, rect)
        data = clamp(getattr(Config, self.name), self.start, self.end)
        percent = (data-self.start)/(self.end-self.start)
        pygame.draw.rect(screen, (47, 161, 214), (start_x, y + 4, new_w * percent, 19))

    def render(self, screen, x, y, w, h, mouse_pos):
        self.render_text(screen, x, y, w)
        self.render_scroll(screen, x, y, w)


class UI:
    def __init__(self, goto_func):
        self.width = 245
        self.button_height = 28
        self.buttons = [ScrollButton((47, 161, 214), 'lat', 'lat', -90, 90),
                        ScrollButton((47, 161, 214), 'lng', 'lng', -180, 180),
                        CheckBoxButton((128, 103, 135), 'isHaloVisible', 'isHaloVisible'),
                        CheckBoxButton((128, 103, 135), 'isPoleVisible', 'isPoleVisible'),
                        CheckBoxButton((128, 103, 135), 'autoSpin', 'autoSpin'),
                        FuncButton((230, 29, 95), 'goToHongKong', lambda: goto_func(22.28552,114.15769)),
                        ScrollButton((47, 161, 214), 'zoom', 'zoom', 0, 1)]
        self.open = True
        self.font = pygame.font.SysFont('sans-serif', 17)
        self.close_text = self.font.render('Close Controls', True, (238,)*3)

    def render(self, screen, screen_w):
        x = screen_w - 15 - self.width
        mouse_pos = pygame.mouse.get_pos()
        if not self.colide_ui(screen_w, mouse_pos) and not self.collide_left(screen_w, mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
        if self.collide_left(screen_w, mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
        if not self.open:
            _rect = pygame.Rect(x, 0, self.width, 20)
            pygame.draw.rect(screen, (0,) * 3, _rect)
            screen.blit(self.close_text, self.close_text.get_rect(center=_rect.center))
            if _rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return
        for i in range(len(self.buttons)):
            self.buttons[i].render_bg(screen, x, i * self.button_height, self.width, self.button_height, mouse_pos)
            self.buttons[i].render(screen, x, i * self.button_height, self.width, self.button_height, mouse_pos)
            self.buttons[i].set_mouse(x, i * self.button_height, self.width, self.button_height, mouse_pos)
        rect = pygame.Rect(x, self.button_height * len(self.buttons), self.width, 20)
        pygame.draw.rect(screen, (0,)*3, rect)
        screen.blit(self.close_text, self.close_text.get_rect(center=rect.center))
        if rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    def collide_left(self, screen_w, mouse_pos):
        if not self.open:
            return False
        x = screen_w - 15 - self.width
        if pygame.Rect(x-3, 0, 6, len(self.buttons) * self.button_height).collidepoint(mouse_pos):
            return True
        return False

    def colide_ui(self, screen_w, mouse_pos):
        x = screen_w - 15 - self.width
        if self.open:
            if pygame.Rect(x+3, 0, self.width-3, len(self.buttons) * self.button_height).collidepoint(mouse_pos):
                return True
            if pygame.Rect(x, self.button_height * len(self.buttons), self.width, 20).collidepoint(mouse_pos):
                return True
            return False
        else:
            return pygame.Rect(x, 0, self.width, 20).collidepoint(mouse_pos)

    def handle_mouse_down(self, screen_w, mouse_pos):
        x = screen_w - 15 - self.width
        if self.open:
            for i in range(len(self.buttons)):
                self.buttons[i].handle_mouse_down(mouse_pos, x, i * self.button_height, self.width, self.button_height)
            if pygame.Rect(x, self.button_height * len(self.buttons), self.width, 20).collidepoint(mouse_pos):
                self.open = not self.open

    def handle_mouse(self, screen_w, mouse_pos):
        if self.open:
            x = screen_w - 15 - self.width
            for i in range(len(self.buttons)):
                if not self.buttons[i].all_down:
                    continue
                self.buttons[i].handle_mouse_down(mouse_pos, x, i * self.button_height, self.width, self.button_height)
