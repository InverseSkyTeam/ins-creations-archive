import pygame
from utils import get_width


def init(caption: str = "TermEd"):
    pygame.init()
    pygame.font.init()
    ui = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption(caption)
    return ui


def is_cn_char(ch: str):
    return get_width(ch) == 2


def render(ui: pygame.Surface, pos, text: str, fg, bg,
           font: tuple, fsize):
    if not text:
        return
    cur = text[0]
    tp = is_cn_char(text[0])
    for i in range(1, len(text)):
        new = is_cn_char(text[i])
        if tp != new:
            cur_surf = font[tp].render(cur, True, fg, bg)
            ui.blit(cur_surf, (pos if not tp else (pos[0], pos[1] - fsize / 5)))
            pos = pos[0] + cur_surf.get_width(), pos[1]
            tp = new
            cur = ""
        cur += text[i]
    if cur:
        ui.blit(font[tp].render(cur, True, fg, bg), (pos if not tp else (pos[0], pos[1] - fsize / 5)))


def main():
    FONT_SIZE = 20
    FPS = 60

    ui = init()
    font = (pygame.font.SysFont("Times New Roman", FONT_SIZE),
            pygame.font.SysFont("Microsoft YaHei", FONT_SIZE))

    font_h = font[1].get_height()
    ed_quit = False

    clock = pygame.time.Clock()
    dt = 0

    while not ed_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ed_quit = True

        nlines = ui.get_height() // font_h

        ui.fill('white')
        for i in range(nlines):
            render(ui, (0, i * font_h),
                   "Hello,你好，world!世界！", 'black', None, font, FONT_SIZE)
        # render(ui, (0, 0),
        #        "Hello, world! 你好，世界！ Hello, TermEd! 你好，TermEd！", 'black', None, font, FONT_SIZE)
        pygame.display.update()

        dt = clock.tick(FPS)
    
    pygame.quit()


if __name__ == "__main__":
    main()
