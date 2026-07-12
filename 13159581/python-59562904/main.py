import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

menu_options = ["复制", "粘贴", "剪切"]
menu_font = pygame.font.Font('CHSansSC.ttf', 14)
menu_item_height = 30
menu_width = 150

menu_bg_color = (255, 255, 255)
menu_hover_color = (0, 95, 184)
text_color = (0, 0, 0)
border_color = (0xd4, 0xd4, 0xd4)

border_radius = 10

menu_visible = False
menu_x = 0
menu_y = 0
menu_direction_up = False

clock = pygame.time.Clock()

running = True
while running:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            menu_visible = True
            menu_x, menu_y = event.pos
            menu_height = len(menu_options) * menu_item_height
            if menu_y + menu_height > height:
                menu_direction_up = True
                new_menu_y = menu_y - menu_height
                menu_y = max(0, new_menu_y)
            else:
                menu_direction_up = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            menu_visible = False

    screen.fill((255, 255, 255))

    if menu_visible:
        menu_rect = pygame.Rect(menu_x, menu_y, menu_width, len(menu_options) * menu_item_height)
        pygame.draw.rect(screen, menu_bg_color, menu_rect, border_radius=border_radius)
        pygame.draw.rect(screen, border_color, menu_rect, width=1, border_radius=border_radius)

        for i, option in enumerate(menu_options):
            text = menu_font.render(option, True, text_color)
            if menu_direction_up:
                option_y = menu_y + i * menu_item_height
            else:
                option_y = menu_y + i * menu_item_height

            item_rect = pygame.Rect(menu_x, option_y, menu_width, menu_item_height)

            if item_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, menu_hover_color, item_rect, border_radius=border_radius)

            screen.blit(text, (menu_x + 10, option_y + 10))

    pygame.display.flip()
    clock.tick(114514)

pygame.quit()