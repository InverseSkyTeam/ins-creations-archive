import pygame
import time
from control import Control


class BaseSkill:
    def __init__(self, filename, rect, cool_time, duration, control, key):
        assert cool_time > duration
        img = pygame.image.load(filename)
        self.img = pygame.transform.smoothscale(img, rect.size).convert_alpha()
        self.rect: pygame.Rect = rect
        self.cool_time = cool_time
        self.duration = duration
        self.last_time = 0

        self.control: Control = control
        self.key = key
        self.font = pygame.font.SysFont('Arial', 50)

    def on_key_down(self, event_key):
        if event_key == self.key and time.time() - self.last_time >= self.cool_time:
            self.last_time = time.time()

    def on_use(self):
        pass

    def on_no_use(self):
        pass

    def update(self):
        if time.time() - self.last_time <= self.duration:
            self.on_use()
        else:
            self.on_no_use()

    def on_resize(self, w, h):
        pass

    def render(self, screen):
        if time.time() - self.last_time <= self.cool_time:
            pygame.draw.circle(screen, (127, 127, 127), self.rect.center, self.rect.w//2)
            remain_time = str(self.cool_time - int(time.time() - self.last_time))
            txt = self.font.render(remain_time, True, (255,) * 3)
            screen.blit(txt, txt.get_rect(center=self.rect.center))
        else:
            screen.blit(self.img, self.rect)


class SwiftnessSkill(BaseSkill):  # 迅捷技能
    def __init__(self, control, w, h):
        super().__init__('data/skill/swiftness.png', pygame.Rect(0, 0, 75, 75),
                         cool_time=10, duration=5, control=control, key=pygame.K_1)
        self.on_resize(w, h)

    def on_use(self):
        self.control.target_fps = 60

    def on_no_use(self):
        self.control.target_fps = 30

    def on_resize(self, w, h):
        self.rect.x = 20
        self.rect.y = h - 110


class SharpnessSkill(BaseSkill):  # 伤害提升
    def __init__(self, control, w, h):
        super().__init__('data/skill/sharpness.png', pygame.Rect(0, 0, 75, 75),
                         cool_time=15, duration=5, control=control, key=pygame.K_2)
        self.on_resize(w, h)

    def on_use(self):
        self.control.add_attack = True

    def on_no_use(self):
        self.control.add_attack = False

    def on_resize(self, w, h):
        self.rect.x = 140
        self.rect.y = h - 110
