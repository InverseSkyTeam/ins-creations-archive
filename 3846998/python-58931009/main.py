import utils
import pygame
import time


def init(caption: str = "TermEd"):
    utils.init()
    ui = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption(caption)
    # print(*zip(utils.font_family, utils.font_shift))
    return ui


def draw(ui: pygame.Surface, pos: utils.Pos, text: str, fg='black', bg='white'):
    if not text:
        return
    tp = utils.pick_font(text[0])
    cur_text = text[0]
    for ch in text[1:]:
        if (ch_tp := utils.pick_font(ch)) != tp:
            if cur_text:
                # print(cur_text, tp, len(cur_text))
                ui.blit((surf := utils.font_instance[tp].render(cur_text, True, fg, bg)),
                        (pos[0], pos[1] + utils.font_shift[tp]))
            tp = ch_tp
            cur_text = ""
            pos = pos[0] + surf.get_width(), pos[1]
        cur_text += ch
    if cur_text:
        ui.blit(utils.font_instance[tp].render(cur_text, True, fg, bg),
                (pos[0], pos[1] + utils.font_shift[tp]))


def main():
    ui = init()
    dt = 0
    clock = pygame.time.Clock()
    FPS = 600
    t = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                ...

        ui.fill("white")

        for i in range(ui.get_height() // (utils.max_size + utils.line_padding) - 1):
            draw(ui, (0, i * (utils.max_size + utils.line_padding)), "Hello, 世界！你好，world!")
        draw(ui, (0, ui.get_height() - (utils.max_size + utils.line_padding)),
             "FPS: " + str(1 / (time.time() - t)))
        t = time.time()

        pygame.display.update()

        dt = clock.tick(FPS)


if __name__ == "__main__":
    main()
