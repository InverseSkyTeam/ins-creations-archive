import pygame
import sys
from INS_Animation import transition, TransitionGroup


pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
clock = pygame.time.Clock()


class Button:
    def __init__(self):
        self.center = (400, 300)
        self.w, self.h = 200, 100

        self.is_hover = False

        self.hover_transition = TransitionGroup()
        self.no_hover_transition = TransitionGroup()

        hover_transition_w = transition((self, 'w', self.w * 1.5), '0.1s', 'ease-in-out', '0s')
        hover_transition_h = transition((self, 'h', self.h * 1.5), '0.1s', 'ease-in-out', '0s')
        self.hover_transition.add_transition([hover_transition_w, hover_transition_h])

        no_hover_transition_w = transition((self, 'w', self.w), '0.1s', 'ease-in-out', '0s')
        no_hover_transition_h = transition((self, 'h', self.h), '0.1s', 'ease-in-out', '0s')
        self.no_hover_transition.add_transition([no_hover_transition_w, no_hover_transition_h])

    def get_rect(self):  # 这个不需要看懂
        rect = pygame.Rect(0, 0, round(self.w), round(self.h))
        rect.center = self.center
        return rect

    def render(self, screen):  # 不用看，只是用于绘制的
        pygame.draw.rect(screen, (255, 0, 0), self.get_rect(), border_radius=20)

        txt = pygame.font.SysFont('SimHei', round(self.w / 10)).render('这是一个按钮', True, (255, 255, 255))
        screen.blit(txt, txt.get_rect(center=self.get_rect().center))

    def handle_event(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.get_rect().collidepoint(mouse_pos):  # 被鼠标碰到
            if not self.is_hover:  # 但是不处于 hover 状态
                self.is_hover = True
                self.no_hover_transition.stop()
                self.hover_transition.start()
        else:  # 没被鼠标碰到
            if self.is_hover:  # 但是处于 hover 状态
                self.is_hover = False
                self.hover_transition.stop()
                self.no_hover_transition.start()

    def update(self):
        self.hover_transition.update()
        self.no_hover_transition.update()


button = Button()


while 1:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            w, h = screen.get_size()
    button.handle_event()

    screen.fill((255,)*3)
    button.update()
    button.render(screen)

    pygame.display.flip()
    clock.tick(114514)
