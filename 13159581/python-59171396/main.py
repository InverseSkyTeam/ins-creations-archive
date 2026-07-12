import pygame
import tkinter as tk
import os

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '240,60'
screen = pygame.display.set_mode((800, 600))

root = tk.Tk()
root.geometry("800x600+240+60")
root.attributes("-topmost", True)
root.attributes("-transparentcolor","#f0f0f0")
root.overrideredirect(True)
popupmenu = tk.Menu(root, bg="#FFFFFF", 
    font=("Arial", 16), tearoff=False,
    activebackground="#005FB8", activeforeground="white")
popupmenu.add_command(label="Test1")
popupmenu.add_command(label="Test2")
popupmenu.add_command(label="Test3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            root.destroy()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                x, y = root.winfo_x(), root.winfo_y()
                popupmenu.post(x + event.pos[0], y + event.pos[1])
        if event.type == pygame.WINDOWMOVED:
            position = event.x, event.y
            root.wm_geometry(f"+{int(position[0])}+{int(position[1])}")


    screen.fill((255, 255, 255))
    root.update()

    pygame.display.update()
