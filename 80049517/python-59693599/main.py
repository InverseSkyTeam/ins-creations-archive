import pygame
from simple_menu import Menu

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def selected_menu_item(index: int):
    global is_show_menu
    print("Selected Menu Item", menu.items[index])
    is_show_menu = False

menu = Menu()
menu.set_items(["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"])
menu.pos = (10, 10)
menu.selected.connect(selected_menu_item)

is_show_menu = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.constants.MOUSEBUTTONDOWN:
            if not menu.is_in_the_menu(event.pos):
                is_show_menu = False
            if event.button == 3:
                menu.pos = event.pos
                is_show_menu = True
        if is_show_menu:
            menu.event_filter(event)

    screen.fill((255, 0, 0))
    if is_show_menu:
        menu.render(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
