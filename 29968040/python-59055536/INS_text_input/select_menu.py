from .selected_manager import SelectedManager
import pygame


class Button:
    def __init__(self, name, call_back):
        self.rect = pygame.Rect(0, 0, 80, 30)
        self.name = name
        self.call_back = call_back
        self.font = pygame.font.SysFont('SimHei', 20)
        self.text = self.font.render(name, True, (0,) * 3)

    def set_pos(self, x, y):
        self.rect.x, self.rect.y = x, y

    def render(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (220,)*3, self.rect, border_radius=5)
        else:
            pygame.draw.rect(screen, (255,)*3, self.rect, border_radius=5)
        screen.blit(self.text, self.text.get_rect(center=self.rect.center))

    def on_mouse_down(self, pos):
        if self.rect.collidepoint(pos):
            self.call_back()


class SelectMenu:
    def __init__(self, selected_manager):
        self.show = False
        self.x, self.y = 0, 0

        self.selected_manager: SelectedManager = selected_manager

        self.buttons = []
        self.cache_button = []

    def set_button_data(self, func_dict: dict):
        self.cache_button = [Button(*data) for data in func_dict.items()]

    def render(self, screen, mouse_pos):
        if not self.show:
            return
        pygame.draw.rect(screen, (255,) * 3, self.rect, border_radius=5)
        for button in self.buttons:
            button.render(screen, mouse_pos)
        pygame.draw.rect(screen, (0,) * 3, self.rect, width=1, border_radius=5)

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 80, 30 * len(self.buttons))

    def on_mouse_down(self, pos):
        for button in self.buttons:
            button.on_mouse_down(pos)

    def add_button(self, button, delta_y):
        button.set_pos(self.x, self.y+delta_y)
        self.buttons.append(button)

    def open_menu(self, x, y):
        self.selected_manager.in_selected = False
        self.show = True
        self.x, self.y = x, y

        if self.selected_manager.have_text:  # 复制 粘贴 全选 剪切
            self.add_button(self.cache_button[0], 0)
            self.add_button(self.cache_button[1], 30)
            self.add_button(self.cache_button[2], 60)
            self.add_button(self.cache_button[3], 90)
        else:  # 粘贴 全选
            self.add_button(self.cache_button[1], 0)
            self.add_button(self.cache_button[2], 30)

    def close_menu(self):
        self.show = False
        self.buttons = []
