import pygame


def set_font(self, font_size, font_style):
    """
    设置渲染的字体
    :param self: MarkdownRenderer类
    :param font_size: 字体大小
    :param font_style: 字体的样式列表
    :return: 字体
    """
    if 'strong' in font_style:  # 粗体
        if self.fonts_bold[round(font_size)]:
            font = self.fonts_bold[round(font_size)]
            try:
                font.set_strikethrough(False)
            except:
                pass
            font.set_italic(False)
        else:
            font = pygame.font.Font('HarmonyOS_Sans_SC_Bold.ttf', round(font_size))
            self.fonts_bold[round(font_size)] = font
    else:  # 非粗体
        if self.fonts[round(font_size)]:
            font = self.fonts[round(font_size)]
            try:
                font.set_strikethrough(False)
            except:
                pass
            font.set_italic(False)
        else:
            font = pygame.font.Font('HarmonyOS_Sans_SC_Regular.ttf', round(font_size))
            self.fonts[round(font_size)] = font
    if 'em' in font_style:  # 斜体
        font.set_italic(True)
    if 's' in font_style:  # 删除线
        try:
            font.set_strikethrough(True)
        except:
            pass
    return font
