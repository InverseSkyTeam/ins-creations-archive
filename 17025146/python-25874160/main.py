import pygame,random
import tkinter as tk
from tkinter import *
import os
root = tk.Tk()
embed = tk.Frame(root, width = 500, height = 500)
embed.pack()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

import platform
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(0,255,255))

pygame.display.update()
root.mainloop()