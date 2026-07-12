import pygame
import math
import time


class CancelText:  # 渲染 “按 ESC 可显示鼠标光标” 的提示
    def __init__(self):
        self.start_time = None
        self._sino = lambda x: math.sin(x * (math.pi / 2))

        w, h = 150 + 50, 40
        self.sf = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.rect(self.sf, (0, 0, 0), (0, 0, w, h), border_radius=5)
        text = pygame.font.SysFont('SimHei', int(h // 2.5)).render('按 ESC 可显示鼠标光标', True, (255,) * 3)
        self.sf.blit(text, text.get_rect(center=self.sf.get_rect().center))

    def start_anim(self):
        self.start_time = time.time()

    def end_anim(self):
        self.start_time = None

    def render(self, screen):
        if not self.start_time:
            return
        time_sub = time.time() - self.start_time
        if time_sub < 0.4:
            num = self._sino(time_sub / 0.4)
            w = int(150 + 50 * num)
            h = int(w / 5)
            alpha = int(150 * num)
        elif 0.4 <= time_sub < 3.4:
            w, h, alpha = 150 + 50, 40, 150
        elif 3.4 <= time_sub < 4.4:
            w, h, alpha = 150 + 50, 40, int(150 - 150 * (time_sub - 3.4))
        else:
            self.end_anim()
            return
        self.sf.set_alpha(alpha)
        screen.blit(pygame.transform.smoothscale(self.sf, (w, h)), ((screen.get_width()-w)//2, 30 + (40 - h) // 2))
