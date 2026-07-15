# cgame/base.py

from typing import Tuple

RGB = Tuple[int, int, int]
POS = Tuple[int, int]
SIZE = Tuple[int, int]

# cgame/surface.py

class Surface(object):
    def __init__(self, size: SIZE) -> None:
        self._pixels: list[list[RGB]] = []
        self._size: SIZE = size

        for i in range(size[0]):
            self._pixels.append([])
            for _ in range(size[1]):
                self._pixels[i].append((255, 255, 255))

    def set_pixel(self, pos: POS, color: RGB):
        self._pixels[pos[0]][pos[1]] = color

    def blit(self, source: "Surface", dest: POS) -> None:
        size = (max(min(source._size[0], self._size[0] - dest[0]), 0), max(min(source._size[1], self._size[1] - dest[1]), 0))
        for top in range(size[0]):
            for left in range(size[1]):
                self._pixels[top + dest[0]][left + dest[1]] = source._pixels[top][left]

    def fill(self, color: RGB) -> None:
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                self._pixels[i][j] = color

# cgame/display.py

import sys

class Display(object):
    def __init__(self) -> None:
        self._pixels: list[list[RGB]] = []
        self._size: SIZE = (0, 0)
        self._inited = False
        self._changed = True

    def set_mode(self, width: int, height: int) -> None:
        if self._inited:
            raise Exception("Cannot re init!")
        self._inited = True
        self._size = (width, height)

        self._pixels.clear()
        for i in range(width):
            self._pixels.append([])
            for _ in range(height):
                self._pixels[i].append((0, 0, 0))
        sys.stdout.write("\033[2J\033[?25l")
        sys.stdout.flush()

    def fill(self, color: RGB) -> None:
        if not self._inited:
            raise Exception("Not inited!")

        for i in range(self._size[0]):
            for j in range(self._size[1]):
                if self._pixels[i][j] != color:
                    self._changed = True
                self._pixels[i][j] = color

    def update(self) -> None:
        if not self._inited:
            raise Exception("Not inited!")

        if not self._changed:
            return
        self._changed = False

        # simple
        # text = "\033[H"
        # for line in self._pixels:
        #     last_color = (0, 0, 0)
        #     text += "\033[48;2;0;0;0m"
        #     for color in line:
        #         if not color == last_color:
        #             last_color = color
        #             text += f"\033[48;2;{color[0]};{color[1]};{color[2]}m"
        #         text += "  "
        #     text += "\033[0m\n"
        # sys.stdout.write(text[:-1])
        # sys.stdout.flush()

        # ▄▄▄
        text = "\033[H"
        for x in range(0, self._size[0], 2):
            last_top = (0, 0, 0)
            last_bottom = (0, 0, 0)
            text += "\033[48;2;0;0;0m\033[38;2;0;0;0m"
            for y in range(0, self._size[1]):
                top_color = self._pixels[x][y]
                if x == self._size[0] - 1:
                    bottom_color = (0, 0, 0)
                else:
                    bottom_color = self._pixels[x + 1][y]
                if last_top != top_color:
                    text += f"\033[48;2;{top_color[0]};{top_color[1]};{top_color[2]}m"
                    last_top = top_color
                if last_bottom != bottom_color:
                    text += f"\033[38;2;{bottom_color[0]};{bottom_color[1]};{bottom_color[2]}m"
                    last_bottom = bottom_color
                text += f"▄"
            text += "\033[0m\n"
        sys.stdout.write(text[:-1])
        sys.stdout.flush()

    def set_pixel(self, pos: POS, color: RGB):
        if not self._inited:
            raise Exception("Not inited!")

        if self._pixels[pos[0]][pos[1]] != color:
            self._changed = True
        self._pixels[pos[0]][pos[1]] = color

    def blit(self, source: Surface, dest: POS) -> None:
        if not self._inited:
            raise Exception("Not inited!")

        if dest[0] >= self._size[0] or dest[1] >= self._size[1]:
            return

        size = (
            max(min(source._size[0], self._size[0] - dest[0]), 0),
            max(min(source._size[1], self._size[1] - dest[1]), 0),
        )
        for top in range(size[0]):
            for left in range(size[1]):
                if (
                    self._pixels[top + dest[0]][left + dest[1]]
                    != source._pixels[top][left]
                ):
                    self._changed = True
                self._pixels[top + dest[0]][left + dest[1]] = source._pixels[top][left]

    def quit(self) -> None:
        if not self._inited:
            raise Exception("Not inited!")
        self._inited = False
        self._pixels.clear()

        sys.stdout.write("\033[H\033[?25h\033[0m\033[2J")
        sys.stdout.flush()

# cgame/draw.py

def rect(surface: Surface, color: RGB, dest: POS, size: SIZE) -> None:
    new_surface = Surface(size)
    new_surface.fill(color)
    surface.blit(new_surface, dest)

########################################

# utils.py

# 由 DeepSeek R1 生成。
import sys
import os
import termios
import select
import atexit

class _Getch:
    def __init__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        
        # 设置新的终端属性：非规范模式、关闭回显
        new = termios.tcgetattr(self.fd)
        new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
        new[6][termios.VMIN] = 0  # 读取最小字符数
        new[6][termios.VTIME] = 0 # 读取超时（十分之一秒）
        
        # 应用新设置
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, new)
        
        # 注册退出恢复函数
        atexit.register(self._restore)

    def _restore(self):
        """恢复原有终端设置"""
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_settings)

    def kbhit(self):
        """检测是否有键盘输入（非阻塞）"""
        rlist, _, _ = select.select([self.fd], [], [], 0)
        return len(rlist) > 0

    def getch(self):
        """获取单个字符（阻塞模式）"""
        # 等待输入可用
        select.select([self.fd], [], [])
        return os.read(self.fd, 1).decode('utf-8', 'ignore')

# 单例模式实例
_getch = _Getch()

def kbhit():
    return _getch.kbhit()

def getch():
    return _getch.getch()

def get_char():
    ch = ""
    while kbhit():
        ch += getch()
    return ch

# main.py

import time

display = Display()
display.set_mode(25, 25)

pos = [5, 5]
count = 5
running = True
while running:
    try:
        for key in get_char():
            if key == 'w':
                pos[0] -= 1
            elif key == 'a':
                pos[1] -= 1
            elif key == 's':
                pos[0] += 1
            elif key == 'd':
                pos[1] += 1

        if pos[0] < 0:
            pos[0] = 0
        if pos[1] < 0:
            pos[1] = 0
        
        if count >= 5:
            count = 0
            
            display.fill((0, 160, 255))
            rect(display, (0, 0, 0), pos, (5, 5))
            display.update()
            print("\nsize:", display._size, end="", flush=True)
        
        count += 1
        time.sleep(0.05)
    except KeyboardInterrupt:
        running = False
display.quit()

