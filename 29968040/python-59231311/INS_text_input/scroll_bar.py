import pygame


SCROLL_MIN_LENGTH = 10  # 滚动条最小长度
SCROLL_OFFSET = 30  # 鼠标滚轮滚动时滑动的像素数


class ScrollBar:
    def __init__(self, container_length, content_length):
        self.visible = True

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

    def handle_event(self, events, on_scroll_func):
        if not self.visible:
            return
        # on_scroll_func: 滚动条被拖动时执行的函数
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.need_scrollbar():
                    if self.scroll_rect.collidepoint(event.pos[0] - self.rect.x, event.pos[1] - self.rect.y):
                        self.start_dragging()
                        on_scroll_func()
            elif event.type == pygame.MOUSEMOTION:
                if self.scroll_dragging:
                    self.update_scroll_offset(self.scroll_offset + event.rel[0])
                    on_scroll_func()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.stop_dragging()

    def start_dragging(self):
        self.scroll_dragging = True
        self.scroll_color = self.scroll_color_hover

    def stop_dragging(self):
        self.scroll_dragging = False
        self.scroll_color = self.scroll_color_normal

    def render(self, screen):
        if not self.visible:
            return
        pygame.draw.rect(screen, self.scroll_color, self.scroll_rect, border_radius=5)

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

    def handle_event(self, events, rect: pygame.Rect, on_scroll_func):
        if not self.visible:
            return
        # on_scroll_func: 滚动条被拖动时执行的函数
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and self.need_scrollbar():
                    if not rect.collidepoint(event.pos):
                        continue
                    self.update_content_offset(self.content_offset - SCROLL_OFFSET)
                    on_scroll_func()
                if event.button == 5 and self.need_scrollbar():
                    if not rect.collidepoint(event.pos):
                        continue
                    self.update_content_offset(self.content_offset + SCROLL_OFFSET)
                    on_scroll_func()
                if event.button == 1 and self.need_scrollbar():
                    if self.scroll_rect.collidepoint(event.pos[0] - self.rect.x, event.pos[1] - self.rect.y):
                        self.start_dragging()
                        on_scroll_func()
            elif event.type == pygame.MOUSEMOTION:
                if self.scroll_dragging:
                    self.update_scroll_offset(self.scroll_offset + event.rel[1])
                    on_scroll_func()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.stop_dragging()

    def start_dragging(self):
        self.scroll_dragging = True
        self.scroll_color = self.scroll_color_hover

    def stop_dragging(self):
        self.scroll_dragging = False
        self.scroll_color = self.scroll_color_normal

    def render(self, screen):
        if not self.visible:
            return
        pygame.draw.rect(screen, self.scroll_color, self.scroll_rect, border_radius=5)

    @property
    def offset(self):
        return int(self.content_offset)
