import pygame
import os
import sys
from PgMarkdown import PygameMarkdown, Load
import requests
import bs4
from urllib.parse import unquote_to_bytes
import json
LUOGU_TI_NAME = 'P1314'
head = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
}


def get_ti(name):
    url = "https://www.luogu.com.cn/problem/" + name
    res = requests.get(url, headers=head)
    res.encoding = res.apparent_encoding
    soup = bs4.BeautifulSoup(res.text, "lxml")
    text = soup.find_all("script", class_="")[0]
    text = str(text)
    a = text[61:-78]
    b = unquote_to_bytes(a.encode()).decode()
    data = json.loads(b)['currentData']['problem']

    text = '# ' + data['title'] + '\n'
    dic = {'background': '题目背景',
           'description': '题目描述',
           'inputFormat': '输入格式',
           'outputFormat': '输出格式',
           'hint': '提示'}

    def add(name, text, data):
        if data[name] != '':
            text += '\n## ' + dic[name] + '\n\n' + data[name] + '\n'
        return text

    text = add('background', text, data)
    text = add('description', text, data)
    text = add('inputFormat', text, data)
    text = add('outputFormat', text, data)
    for i, sam in enumerate(data['samples']):
        if sam[0][-1] == '\n':
            sam[0] = sam[0][:-1]
        if sam[1][-1] == '\n':
            sam[1] = sam[1][:-1]
        text += '\n## 样例 #' + str(i + 1) + '\n\n### 样例输入 #' + str(i + 1) + '\n\n```\n' + sam[
            0] + '\n```\n\n### 样例输出 #' + str(i + 1) + '\n\n```\n' + sam[1] + '\n```\n'
    text = add('hint', text, data)
    return text


pygame.init()
screenHeight = 650
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("INS-PGM")
clock = pygame.time.Clock()

md = PygameMarkdown.MarkdownRenderer()
# data = Load.Load()
# print(get_ti(LUOGU_TI_NAME))
# data.set_markdown_from_string(get_ti(LUOGU_TI_NAME))
md.load_data(Load.load("./cs1.md"))  # 加载 markdown 文件

md.set_area(surface=screen, offset_x=50, offset_y=10, width=500, height=630)

while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            pass

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (239, 239, 239), (0, 0, screenWidth, screenHeight))

    # 绘制
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed)

    pygame.display.flip()
    clock.tick(120)
