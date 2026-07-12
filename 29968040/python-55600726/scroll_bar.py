import pygame


SCROLL_MIN_LENGTH = 10  # 滚动条最小长度


class ScrollBar:
    def __init__(self, container_length, content_length):
        self.container_length = container_length  # 容器长度
        self.content_length = content_length  # 内容长度

        self.scroll_offset = 0  # 滚动条滚动的距离
        self.scroll_length = 0  # 滚动条长度

        self.content_offset = 0  # 内容滚动的距离

    def need_scrollbar(self):  # 是否需要使用滚动条
        return self.content_length > self.container_length

    def max_scroll_offset(self):
        return self.container_length - self.scroll_length

    def max_content_offset(self):
        return self.content_length - self.container_length

    def update_content_length(self, new_content_length):
        self.content_length = new_content_length
        if self.need_scrollbar():
            self.content_offset = max(0, min(self.content_offset, self.max_content_offset()))
            self.scroll_length = max(self.container_length ** 2 / self.content_length, SCROLL_MIN_LENGTH)
            self.scroll_offset = self.content_offset * self.max_scroll_offset() / self.max_content_offset()
        else:
            self.scroll_offset = 0  # 滚动条滚动的距离
            self.scroll_length = 0  # 滚动条长度
            self.content_offset = 0  # 内容滚动的距离

    def update_container_length(self, new_container_length):
        self.container_length = new_container_length
        self.update_content_length(self.content_length)

    def update_scroll_offset(self, new_scroll_offset):
        if not self.need_scrollbar():
            return
        self.scroll_offset = max(0, min(new_scroll_offset, self.max_scroll_offset()))
        self.content_offset = self.scroll_offset * self.max_content_offset() / self.max_scroll_offset()

    def update_content_offset(self, new_content_offset):
        if not self.need_scrollbar():
            return
        self.content_offset = max(0, min(new_content_offset, self.max_content_offset()))
        self.scroll_offset = self.content_offset * self.max_scroll_offset() / self.max_content_offset()


class HScrollBar(ScrollBar):  # 水平滚动条
    def __init__(self, rect):
        super().__init__(rect.w, 0)
        self.rect = rect
        self.scroll_dragging = False  # 是否在拖动滚动条

        self.scroll_color_normal = pygame.Color(255, 255, 255).lerp((0, 0, 0), 0.25)  # 滚动条颜色
        self.scroll_color_hover = pygame.Color(255, 255, 255).lerp((0, 0, 0), 0.4)  # 鼠标悬停颜色
        self.scroll_color = self.scroll_color_normal

    @property
    def scroll_rect(self):
        return pygame.Rect(self.scroll_offset, self.rect.h - 5, self.scroll_length, 5)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.need_scrollbar():
                    if self.scroll_rect.collidepoint(event.pos[0] - self.rect.x, event.pos[1] - self.rect.y):
                        self.scroll_dragging = True
                        self.scroll_color = self.scroll_color_hover
            elif event.type == pygame.MOUSEMOTION:
                if self.scroll_dragging:
                    self.update_scroll_offset(self.scroll_offset + event.rel[0])
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.scroll_dragging = False
                    self.scroll_color = self.scroll_color_normal

    def render(self, screen):
        pygame.draw.rect(screen, self.scroll_color, self.scroll_rect, border_radius=5)

    def update_rect(self, new_rect):
        self.rect = new_rect
        self.update_container_length(self.rect.w)

    @property
    def offset(self):
        return int(self.content_offset)


class VScrollBar(ScrollBar):  # 竖直滚动条
    def __init__(self, rect):
        super().__init__(rect.h, 0)
        self.rect = rect
        self.scroll_dragging = False  # 是否在拖动滚动条

        self.scroll_color_normal = pygame.Color(255, 255, 255).lerp((0, 0, 0), 0.25)  # 滚动条颜色
        self.scroll_color_hover = pygame.Color(255, 255, 255).lerp((0, 0, 0), 0.4)  # 鼠标悬停颜色
        self.scroll_color = self.scroll_color_normal

    @property
    def scroll_rect(self):
        return pygame.Rect(self.rect.w - 5, self.scroll_offset, 5, self.scroll_length)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and self.need_scrollbar():
                    self.update_content_offset(self.content_offset - 20)
                if event.button == 5 and self.need_scrollbar():
                    self.update_content_offset(self.content_offset + 20)
                if event.button == 1 and self.need_scrollbar():
                    if self.scroll_rect.collidepoint(event.pos[0] - self.rect.x, event.pos[1] - self.rect.y):
                        self.scroll_dragging = True
                        self.scroll_color = self.scroll_color_hover
            elif event.type == pygame.MOUSEMOTION:
                if self.scroll_dragging:
                    self.update_scroll_offset(self.scroll_offset + event.rel[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.scroll_dragging = False
                    self.scroll_color = self.scroll_color_normal

    def render(self, screen):
        pygame.draw.rect(screen, self.scroll_color, self.scroll_rect, border_radius=5)

    def update_rect(self, new_rect):
        self.rect = new_rect
        self.update_container_length(self.rect.h)

    @property
    def offset(self):
        return int(self.content_offset)
