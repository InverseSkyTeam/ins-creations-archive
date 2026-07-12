import pygame
import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import os

music_path = "music/test.wav"
with open('music/test Timer.txt', 'r', encoding='utf-8') as f:
    song_chart = [float(i) for i in f.read().split('\n') if i]
with open('music/test X.txt', 'r', encoding='utf-8') as f:
    x_chart = [float(i) for i in f.read().split('\n') if i]

root = tk.Tk()
root.attributes('-topmost', True)
root.attributes('-transparentcolor', '#f0f0f0')
root.attributes('-fullscreen', True)
root.overrideredirect(True)
tk.Label(root, text='简陋音游 AutoPlay（雾', font=("kaiti", 30)).pack()
tk.Label(root, text='Esc 退出', font=("kaiti", 20)).pack()

os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 330), pygame.NOFRAME)

pygame.mixer.music.load(music_path)
pygame.mixer.music.play()

blues = pygame.mixer.Sound('music/Blue.mp3')
reds = pygame.mixer.Sound('music/Red.wav')
yellows = pygame.mixer.Sound('music/Yellow.mp3')

def play_note(type: int):
    if type == 1:
        blues.play()
    elif type == 7:
        reds.play()
    elif type == 13:
        yellows.play()

class TapNoteTk:
    def __init__(self, x, y, speed, image_num):
        self.is_running = True
        self.top = tk.Toplevel(root)
        self.top.attributes('-topmost', True)
        self.top.attributes('-transparentcolor', '#f0f0f0')
        self.top.overrideredirect(True)
        self.top.geometry(f'120x40+{400+int(x)}+{100+int(y)}')
        self.image_num = image_num
        self.speed = speed
        self.image = Image.open(f'images/作者{self.image_num}.png')
        self.image = self.image.rotate(90,expand=1)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.top, image=self.tk_image)
        self.label.pack()
    def update(self):
        if self.is_running:
            self.top.update()
        self.top.geometry(f'120x40+{self.top.winfo_x()}+{self.top.winfo_y() - self.speed}')
        if self.top.winfo_y() <= 400:
            self.top.destroy()
            self.is_running = False

class TapNote(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image_num = random.choice([1,7,13])
        self.image = pygame.image.load(f'images/作者{self.image_num}.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.tk_top = TapNoteTk(x, y, speed, self.image_num)

    def update(self):
        if self.rect.y <= 50:
            self.kill()
        self.rect.y -= self.speed
        if self.tk_top.is_running:
            self.tk_top.update()

    def kill(self):
        super().kill()
        animations.add(ClickAnimation(self.rect.center))
        play_note(self.image_num)


class ClickAnimation(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.center = center
        self.animation_id = 2
        self.image = pygame.image.load(f'animations/perfect__img-{self.animation_id}.svg').convert_alpha()
        self.rect = self.image.get_rect(center=center)

    def update(self):
        if self.animation_id < 24:
            self.animation_id += 1
            self.image = pygame.image.load(f'animations/perfect__img-{self.animation_id}.svg').convert_alpha()
            self.rect = self.image.get_rect(center=self.center)
        else:
            self.kill()


notes = pygame.sprite.Group()
animations = pygame.sprite.Group()

start_time = time.time()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((123, 123, 123))
    pygame.draw.line(screen, (0, 100, 255), (25, 50), (475, 50))
    pygame.draw.line(screen, (0, 100, 255), (25, 300), (475, 300))

    elapsed_time = time.time() - start_time
    for note_time in song_chart:
        if elapsed_time >= note_time:
            x = x_chart[song_chart.index(note_time)] + 240
            speed = 10
            note = TapNote(x, 700, speed)
            notes.add(note)
            song_chart.remove(note_time)
            x_chart.remove(x - 240)

    notes.update()
    notes.draw(screen)
    animations.update()
    animations.draw(screen)

    pygame.display.flip()
    root.update()
    clock.tick(60)

pygame.quit()
root.destroy()
