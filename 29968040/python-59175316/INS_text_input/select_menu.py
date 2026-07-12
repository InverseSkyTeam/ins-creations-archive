from .selected_manager import SelectedManager
from INS_Animation import transition
from .util import draw_shadow
import pygame
pygame.font.init()

font = pygame.font.Font('CHSansSC.ttf', 14)

normal_font_color = (26, 26, 26)
hover_font_color = (255, 255, 255)

normal_bg_color = (255, 255, 255)
hover_bg_color = (0, 95, 184)

menu_border_color = (0xd4, 0xd4, 0xd4)

button_w, button_h = 196, 26
button_padding = 26
button_margin_w = 204
button_margin_left = 4
button_margin_vertical = 5


class Button:
    def __init__(self, text, func):
        self.normal_text = font.render(text, True, normal_font_color)
        self.hover_text = font.render(text, True, hover_font_color)
        self.func = func

    def render(self, screen, x, y, mouse_pos):
        rect = pygame.Rect(x, y, button_w, button_h)

        if rect.collidepoint(mouse_pos):
            text_rect = self.hover_text.get_rect(midleft=(x + button_padding, rect.centery))
            pygame.draw.rect(screen, hover_bg_color, rect, border_radius=7)
            screen.blit(self.hover_text, text_rect)
        else:
            text_rect = self.normal_text.get_rect(midleft=(x + button_padding, rect.centery))
            pygame.draw.rect(screen, normal_bg_color, rect, border_radius=7)
            screen.blit(self.normal_text, text_rect)

    def on_mouse_down(self, x, y, mouse_pos):
        rect = pygame.Rect(x, y, button_w, button_h)
        if rect.collidepoint(mouse_pos):
            self.func()


class SelectMenu:
    def __init__(self, selected_manager):
        self.is_menu_visible = False
        self.x, self.y = 0, 0
        self.alpha = 0

        self.visible_transition = transition((self, 'alpha', 255), '0.1s', 'ease-in-out')
        self.invisible_transition = transition((self, 'alpha', 0), '0.1s', 'ease-in-out')

        self.selected_manager: SelectedManager = selected_manager

        self.buttons = []
        self.normal_menu_button = []
        self.select_menu_button = []

    def add_normal_menu_button(self, name, func):
        self.normal_menu_button.append(Button(name, func))

    def add_select_menu_button(self, name, func):
        self.select_menu_button.append(Button(name, func))

    def render(self, screen, mouse_pos):
        if self.alpha == 0:
            return
        menu_surface = pygame.Surface((self.rect.w + 2, self.rect.h + 2), pygame.SRCALPHA)
        menu_surface.blit(draw_shadow(*self.rect.size), (2, 2))
        pygame.draw.rect(menu_surface, normal_bg_color, (0, 0, *self.rect.size), border_radius=10)
        x, y = button_margin_left, button_margin_vertical
        mx, my = mouse_pos
        for button in self.buttons:
            button.render(menu_surface, x, y, (mx - self.rect.x, my - self.rect.y))
            y += button_h
        pygame.draw.rect(menu_surface, menu_border_color, (0, 0, *self.rect.size), width=1, border_radius=10)
        menu_surface.set_alpha(self.alpha)
        screen.blit(menu_surface, self.rect)

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, button_margin_w,
                           button_h * len(self.buttons) + 2 * button_margin_vertical)

    def on_mouse_down(self, pos):
        x, y = self.rect.x + button_margin_left, self.rect.y + button_margin_vertical
        for button in self.buttons:
            button.on_mouse_down(x, y, pos)
            y += button_h

    def open_menu(self, x, y):
        self.close_menu()
        self.selected_manager.in_selected = False
        self.is_menu_visible = True
        self.x, self.y = x, y

        if self.selected_manager.has_selection:  # 复制 粘贴 全选 剪切
            self.buttons = self.select_menu_button
        else:  # 粘贴 全选
            self.buttons = self.normal_menu_button

        if self.invisible_transition.play or not self.visible_transition.play:
            self.visible_transition.start()
            self.invisible_transition.stop()

    def update(self):
        self.visible_transition.update()
        self.invisible_transition.update()

    def close_menu(self):
        self.is_menu_visible = False

        if not self.invisible_transition.play or self.visible_transition.play:
            self.visible_transition.stop()
            self.invisible_transition.start()
