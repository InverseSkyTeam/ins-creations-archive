import pygame


class Mod:
    def __init__(self, screen, x):
        img = pygame.image.load('line.png')
        self.img = pygame.Surface((36, 36), pygame.SRCALPHA)
        self.img.blit(img, img.get_rect(center=self.img.get_rect().center))
        self.line_x = x
        self.screen = screen

        self.dragging = False

    def draw(self):
        img_size = int(min(self.screen.get_size()) / 15)
        img_sf = pygame.transform.smoothscale(self.img, (img_size,) * 2)
        line_sf = pygame.Surface((int(img_size*1.5), self.screen.get_height()), pygame.SRCALPHA)
        center_x, center_y = line_sf.get_width() // 2, line_sf.get_height()//2
        pygame.draw.line(line_sf, (255, 255, 255, 166), (center_x, 0), (center_x, self.screen.get_height()))
        pygame.draw.circle(line_sf, (255, 255, 255, 204), (center_x, center_y), center_x)
        line_sf.blit(img_sf, img_sf.get_rect(center=line_sf.get_rect().center))
        self.screen.blit(line_sf, (int(self.screen.get_width()*self.line_x-center_x), 0))

    def on_mouse_motion(self, delta_x):
        if self.dragging:
            self.line_x += delta_x/self.screen.get_width()
            self.line_x = min(max(self.line_x, 0), 1)
            return True
        return False

    def on_mouse_down(self, pos):
        img_size = int(min(self.screen.get_size()) / 15)
        center_x = int(img_size*1.5) // 2
        screen_w, screen_h = self.screen.get_size()
        rect = pygame.Rect(int(screen_w*self.line_x-center_x), screen_h//2-center_x, center_x*2, center_x*2)
        if rect.collidepoint(*pos) and not self.dragging:
            self.dragging = True
            return True
        return False

    def on_mouse_up(self):
        self.dragging = False
