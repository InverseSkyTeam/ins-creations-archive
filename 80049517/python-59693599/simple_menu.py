import pygame
from animation2187 import Animation2187
from simple_signal import Signal, UseSignal
from typing import Tuple, List


MENU_ITEM_WIDTH = 100
MENU_ITEM_HEIGHT = 30

MENU_BG = (255, 255, 255)
MENU_PADDING = 5
MENU_RADIUS = 5

MENU_HOVER_BG = (0, 160, 255)

MENU_FONT_FAMILY = None
MENU_FONT_SIZE = 30
MENU_FONT_COLOR = (0, 0, 0)
MENU_FONT_ANTIALIAS = True


class _MenuItemSprite(pygame.sprite.Sprite):
    """菜单项角色"""

    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((MENU_ITEM_WIDTH, MENU_ITEM_HEIGHT)).convert_alpha()
        self.rect = pygame.rect.Rect(0, 0, MENU_ITEM_WIDTH, MENU_ITEM_HEIGHT)

        self.image.fill((255, 255, 255, 0))
        self.index = 0  # 此选项在菜单的位置

    def set_index(self, index: int):
        """设置项目编号，从 0 开始"""
        self.index = index
        self.rect.top = self.index * (MENU_ITEM_HEIGHT + MENU_PADDING) + MENU_PADDING
        self.rect.left = MENU_PADDING

    def set_text(self, text: str, font: pygame.font.Font):
        """设置项目文本"""
        surface = font.render(text, MENU_FONT_ANTIALIAS, MENU_FONT_COLOR)
        top = MENU_ITEM_HEIGHT // 2 - surface.get_rect().height // 2
        self.image.blit(surface, (MENU_PADDING, top))


class _MenuItemHoverSprite(pygame.sprite.Sprite):
    """菜单 hoverer 角色"""

    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((MENU_ITEM_WIDTH, MENU_ITEM_HEIGHT)).convert_alpha()
        self.rect = pygame.rect.Rect(0, 0, MENU_ITEM_WIDTH, MENU_ITEM_HEIGHT)
        self.animation = Animation2187(self)

        self.image.fill((255, 255, 255, 0))
        pygame.draw.rect(self.image, MENU_HOVER_BG, self.rect, border_radius=MENU_RADIUS)

    def draw(self, surface: pygame.surface.Surface):
        """绘制 hoverer"""
        self.update()
        surface.blit(self.image, self.rect.topleft)

    def update(self):
        """更新 hoverer"""
        self.animation.update()


class Menu(UseSignal):
    """
    ## 简单的 PyGame 菜单组件
    """

    selected: Signal[int]
    """菜单项目选中事件"""

    def __init__(self):
        UseSignal.__init__(self)

        self.surface: pygame.surface.Surface = None
        self.pos: Tuple[int, int] = (MENU_PADDING, MENU_PADDING)
        self.font = pygame.font.Font(MENU_FONT_FAMILY, MENU_FONT_SIZE)

        self.items = []
        self.item_sprites = pygame.sprite.Group()
        self.item_sprites_list = []

        self.hoverer = _MenuItemHoverSprite()
        self.show_hoverer = False

    def set_items(self, items: List[str]):
        """设置菜单项目"""

        self.items = items
        self.surface = pygame.surface.Surface(
            (MENU_ITEM_WIDTH + 2 * MENU_PADDING, (MENU_ITEM_HEIGHT + MENU_PADDING) * len(items) + MENU_PADDING)
        ).convert_alpha()
        self.item_sprites.remove(self.item_sprites_list)

        for index, item in enumerate(items):
            sprite = _MenuItemSprite()
            sprite.set_text(item, self.font)
            sprite.set_index(index)

            self.item_sprites.add(sprite)
            self.item_sprites_list.append(sprite)

    def render(self, screen: pygame.surface.Surface):
        """渲染菜单"""

        self.surface.fill((255, 255, 255, 0))
        pygame.draw.rect(self.surface, MENU_BG, self.surface.get_rect(), border_radius=MENU_RADIUS)

        if self.show_hoverer:
            self.hoverer.draw(self.surface)
        self.item_sprites.draw(self.surface)

        screen.blit(self.surface, self.pos)

    def is_in_the_menu(self, pos: Tuple[int, int]):
        """辅助函数：指定坐标是否在菜单内"""
        left, top = pos
        return (self.pos[1] <= top <= self.pos[1] + self.surface.get_height()) and (
            self.pos[0] <= left <= self.pos[0] + self.surface.get_width()
        )

    def get_current_index(self, pos: Tuple[int, int]):
        """辅助函数：指定坐标在菜单内的第几项（从 0 开始）"""
        return (pos[1] - self.pos[1]) // (MENU_ITEM_HEIGHT + MENU_PADDING)

    def event_filter(self, event: pygame.event.Event):
        """事件过滤处理器"""

        if event.type == pygame.constants.MOUSEMOTION:
            if self.is_in_the_menu(event.pos):
                self.show_hoverer = True
                current_index = self.get_current_index(event.pos)
                hoverer_top = (MENU_ITEM_HEIGHT + MENU_PADDING) * current_index + MENU_PADDING
                self.hoverer.animation.move((MENU_PADDING, hoverer_top), 0.5)
            else:
                self.show_hoverer = False
        elif event.type == pygame.constants.MOUSEBUTTONUP:
            if self.is_in_the_menu(event.pos) and event.button == 1:
                current_index = self.get_current_index(event.pos)
                self.show_hoverer = False
                self.selected.emit(current_index)
