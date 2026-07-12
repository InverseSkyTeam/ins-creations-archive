import pygame, bs4


def render_text(screen, blocks, block_type,
                normal_font, normal_font_size, code_font, code_font_size, font_color,
                start_x, start_y, end_x, line_start_x, line_height):
    if "设置字体模式":
        if block_type == 'strong' and not normal_font.get_bold():
            normal_font.set_bold(True)
            code_font.set_bold(True)
        elif block_type == 'em':
            normal_font.set_italic(True)
            code_font.set_italic(True)
        elif block_type == 'a':
            font_color = (0x34, 0x98, 0xdb)
        elif block_type == 's':
            normal_font.set_strikethrough(True)
            code_font.set_strikethrough(True)
        elif block_type[0] == 'h':
            normal_font.set_bold(True)
            code_font.set_bold(True)
    x, y = start_x, start_y
    for num, i in enumerate(blocks):
        if str(type(i)) == "<class 'bs4.element.NavigableString'>":
            if str(i) == '\n':
                continue
            txt = str(i)
            if blocks[num-1].name == 'br':
                txt = txt[1:]
            x, y = render_txt(screen, txt, normal_font, normal_font_size, font_color, line_height,
                              x, y, end_x, line_start_x)
        elif i.name == 'br':
            x, y = start_x, y + line_height * normal_font_size
        elif i.name in ['strong', 'em', 's', 'a']:
            x, y = render_text(screen, i.contents, i.name, normal_font, normal_font_size, code_font, code_font_size, font_color,
                               x, y, end_x, line_start_x, line_height)
    if "还原字体":
        if block_type == 'strong':
            normal_font.set_bold(False)
            code_font.set_bold(False)
        elif block_type == 'em':
            normal_font.set_italic(False)
            code_font.set_italic(False)
        elif block_type == 'a':
            font_color = (0, 0, 0)
        elif block_type == 's':
            normal_font.set_strikethrough(False)
            code_font.set_strikethrough(False)
        elif block_type[0] == 'h':
            normal_font.set_bold(False)
            code_font.set_bold(False)
    return x, y


def render_txt(screen, text, font1, font_size, font_color, line_height,
               start_x, start_y, end_x, line_start_x):
    font = font1
    if font.get_bold():
        font = pygame.font.Font('HarmonyHeiTiBold.ttf', font_size)
        if font1.get_italic():
            font.set_italic(True)
        try:
            if font1.get_strikethrough():
                font.set_strikethrough(True)
        except:
            pass
    text = text.replace('\n', ' ')
    offest = (line_height-1)*font_size

    current_line = ""
    for word in text:
        temp_line = current_line + word if current_line != "" else word
        if font.size(temp_line)[0] > end_x-start_x:
            screen.blit(font.render(current_line, True, font_color),(start_x, start_y+offest/2))
            current_line = word
            start_x = line_start_x
            start_y += line_height*font_size
        else:
            current_line = temp_line
    screen.blit(font.render(current_line, True, font_color), (start_x, start_y + offest / 2))
    return start_x + font.size(current_line)[0], start_y
