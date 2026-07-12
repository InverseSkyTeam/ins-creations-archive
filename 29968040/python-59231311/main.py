import pygame
import sys
import os
from INS_text_input import TextInput


def install_library():
    try:
        import pygame
        print("pygame当前版本：", pygame.version.vernum)
        if not (pygame.version.vernum.major >= 2 and pygame.version.vernum.minor >= 3):
            raise ValueError
    except ValueError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        import sys
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', "--upgrade", "pygame"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)


install_library()

os.environ["SDL_IME_SHOW_UI"] = "1"

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("pygame多行文本编辑器·重生")

pygame.key.set_repeat(450, 25)

clock = pygame.time.Clock()

with open('./demo.txt', 'r', encoding='utf-8') as f:
    _init_text = str(f.read())
# with open('./example.js', 'r', encoding='utf-8') as f:
#     _init_text = str(f.read())

entry_box = TextInput(screen_rect=screen.get_rect(),
                      font=pygame.font.Font('CHSansSC.ttf', 16),
                      font_size=16, font_color=(0, )*3, line_height=24,
                      rect=pygame.Rect(10, 10, w - 20, 24),
                      init_text=_init_text, multi_lines=False)
entry_box.hScroll.visible = False

input_box = TextInput(screen_rect=screen.get_rect(),
                      font=pygame.font.Font('CHSansSC.ttf', 16),
                      font_size=16, font_color=(0, )*3, line_height=24,
                      rect=pygame.Rect(10, 10 + 34, w - 20, h - 20 - 34),
                      init_text=_init_text, multi_lines=True)


while True:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    pygame_events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,)*3)
    pygame.draw.rect(screen, (0xdd,) * 3, input_box.rect.inflate(4, 4), width=2)
    input_box.handle_events(pygame_events, mouse_pos)
    input_box.display(screen, mouse_pos)

    pygame.draw.rect(screen, (0xdd,) * 3, entry_box.rect.inflate(4, 4), width=2)
    entry_box.handle_events(pygame_events, mouse_pos)
    entry_box.display(screen, mouse_pos)
    # input_box.debug()

    pygame.display.update()
    clock.tick(114514)
