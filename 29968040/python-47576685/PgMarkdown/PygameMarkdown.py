import pygame
import re
import markdown2
import bs4
from . import _html_label
import pygame.gfxdraw

class MarkdownRenderer:
    def __init__(self):
        self.x: int = None
        self.y: int = None
        self.w: int = None
        self.h: int = None
        self.margin: int = None
        self.screen: pygame.Surface = None  # 用于存储边框、背景的画布
        self.text_screen: pygame.Surface = None  # 专门存储文字、图片的画布
        self.a_rects: list = []  # 存储超链接的rect

        # 颜色
        self.color_area_background = (255, 255, 255)  # 背景颜色
        self.color_href = (0x34, 0x98, 0xdb)  # 超链接颜色
        self.color_href_hover = (0x14, 0x55, 0x8f)  # 超链接鼠标悬停颜色

        # 字体
        self.font_normal_size = 16

        self.html = ""
        self.blocks = None
        self.background_rendering = True  # 是否渲染背景

    def set_markdown(self, mdfile_path):
        # 加载 md 文件并解析为 HTML
        with open(mdfile_path, "r", encoding='utf-8') as f:
            md_string = ''.join(list(f))
        self.set_markdown_from_string(md_string)

    def set_markdown_from_string(self, md_string):
        # 从字符串加载 md 代码并解析为 HTML
        for i in ['bash', 'c', 'cs', 'cpp', 'd', 'dart', 'erlang', 'erlang-repl', 'go', 'groovy',
                  'handlebars', 'hbs', 'haskell', 'hs', 'html', 'java', 'javascript', 'js', 'json',
                  'kotlin', 'lisp', 'lua', 'matlab', 'objectivec', 'perl', 'php', 'powershell', 'ps1',
                  'psm1', 'puppet', 'python', 'py', 'r', 'rss', 'ruby', 'rb', 'rust', 'scala', 'sql',
                  'swift', 'vbnet', 'typescript', 'ts', 'xml', 'yaml', 'yml']:
            md_string = re.sub(r'```\s*'+i, '```\n'+i, md_string)
        self.html = markdown2.markdown(md_string, extras=['fenced-code-blocks', 'strike',
                                                          'cuddled-lists', 'tables', 'tag-friendly'])
        self.html = '<html><head></head><body>'+self.html.replace('&amp;', '&')+'</body></html>'
        #print(self.html)
        self.blocks = None
        self.parse_markdown_file()

    def parse_markdown_file(self):
        self.blocks = bs4.BeautifulSoup(self.html, 'lxml').body
        li_tags = self.blocks.find_all('li')
        for li in li_tags:
            ol_tags = li.find_all('ol')
            ul_tags = li.find_all('ul')
            for ol in ol_tags:
                ol.name = 'ol_nest'
            for ul in ul_tags:
                ul.name = 'ul_nest'

        #self.blocks = self.blocks.contents
        print(self.blocks)

    def set_area(self, surface, offset_x, offset_y, width=-1, height=-1, margin=10) -> None:
        """
        设置 Markdown 渲染区域的位置和大小
        :param surface: 渲染到的 pygame Surface 对象
        :param offset_x: 相对于 Surface 左上角的 X 偏移量
        :param offset_y: 相对于 Surface 左上角的 Y 偏移量
        :param width: 渲染区域的宽度，默认为 -1，表示使用 Surface 的宽度
        :param height: 渲染区域的高度，默认为 -1，表示使用 Surface 的高度
        :param margin: 渲染区域与边界的间距，默认为 10
        :return: None
        """
        self.margin = margin
        # 为了简化计算，将间距从初始的 x、y、w 和 h 中减去。
        # 在渲染背景矩形时，我们将间距添加回来。
        # 这样，间距对其他计算没有任何影响。

        self.x = offset_x + margin
        self.y = offset_y + margin
        # 如果没有给定值，我们将取 Surface 的边界作为限制。
        self.w = width - (2 * self.margin) if width > 0 else surface.get_width() - offset_x - (2 * self.margin)
        self.h = height - (2 * self.margin) if height > 0 else surface.get_height() - offset_y - (2 * self.margin)
        self.pixels_showable_at_once = self.h
        self.screen = surface
        self.text_screen = pygame.Surface((surface.get_width(), surface.get_height()), pygame.SRCALPHA)

    def set_font(self, font_size, font_style):
        font = None
        if 'strong' in font_style:
            font = pygame.font.Font('HarmonyHeiTi Bold.ttf', round(font_size))
        else:
            font = pygame.font.Font('HarmonyHeiTi Medium.ttf', round(font_size))
        if 'em' in font_style:
            font.set_italic(True)
        if 's' in font_style:
            font.set_strikethrough(True)
        return font

    def render_txt(self, text, font_size, font_color, font_style, line_height,
                   start_x, start_y, end_x, line_start_x):
        font = self.set_font(font_size, font_style)
        text = text.replace('\n', ' ')
        line_height *= font_size

        current_line = ""
        text_rect = []
        for word in text:
            temp_line = current_line + word if current_line != "" else word
            if font.size(temp_line)[0] > end_x - start_x:
                font_surface = font.render(current_line, True, font_color)
                self.text_screen.blit(font_surface, (start_x, start_y +
                                                     (line_height - font_surface.get_height()) / 2))
                text_rect.append(pygame.Rect(start_x,
                                             start_y + (line_height - font_surface.get_height()) / 2,
                                             font_surface.get_width(),
                                             font_surface.get_height()))
                current_line = word
                start_x = line_start_x
                start_y += line_height
            else:
                current_line = temp_line
        font_surface = font.render(current_line, True, font_color)
        self.text_screen.blit(font_surface, (start_x, start_y +
                                             (line_height - font_surface.get_height()) / 2))
        text_rect.append(pygame.Rect(start_x,
                                     start_y + (line_height - font_surface.get_height()) / 2,
                                     font_surface.get_width(),
                                     font_surface.get_height()))
        return [start_x + font.size(current_line)[0], line_start_x], [start_y, start_y+line_height], text_rect

    def render_code(self, font_size, font_style, code):
        label = _html_label.code()
        data = label.data
        self_font_size = data.calc_pos(label.font_size, font_size, self.font_normal_size)
        data.calc_style(self_font_size, self.font_normal_size)
        font = self.set_font(self_font_size, font_style)
        code_surface = font.render(code, True, (0, 0, 0))
        surface = pygame.Surface((data.margin_left+data.border_left_width+data.padding_left+
                                  code_surface.get_width()+
                                  data.margin_right + data.border_right_width + data.padding_right,
                                  data.border_top_width+data.padding_top+
                                  code_surface.get_height()+
                                  data.padding_bottom+data.border_bottom_width), pygame.SRCALPHA)
        pygame.draw.rect(surface, data.background_color, (data.margin_left, data.margin_top,
                                                          data.border_left_width + data.padding_left +
                                                          code_surface.get_width() +
                                                          data.border_right_width + data.padding_right,
                                                          data.padding_top +
                                                          code_surface.get_height() +
                                                          data.padding_bottom
                                                          ),border_radius=2)
        pygame.draw.rect(surface, data.border_left_color, (data.margin_left, data.margin_top,
                                                          data.border_left_width + data.padding_left +
                                                          code_surface.get_width() +
                                                          data.border_right_width + data.padding_right,
                                                          data.padding_top +
                                                          code_surface.get_height() +
                                                          data.padding_bottom
                                                          ), width=data.border_left_width, border_radius=2)
        surface.blit(code_surface, (data.margin_left+data.border_left_width+data.padding_left,
                                    data.border_top_width+data.padding_top))
        return surface

    def render(self, blocks, font_size, font_color, font_style,
               start_pos, end_x, line_start_x, last_margin_bottom, list_start=None):
        x, y = start_pos
        block_contents = blocks.contents
        while block_contents[-1] == '\n':
            block_contents.pop()
        rects = []
        for i, block in enumerate(block_contents):
            if str(type(block)) == "<class 'bs4.element.NavigableString'>":
                txt = str(block)
                if txt == '\n':
                    continue
                if i > 1 and blocks.contents[i - 1].name == 'br':
                    txt = txt[1:]
                x, y, rect = self.render_txt(txt, font_size, font_color, font_style, 1.5,
                                             x[0], y[0], end_x, line_start_x)
                rects.append(rect)
            if block.name in ['strong', 'em', 's', 'a', 'img', 'br', 'code']:
                if block.name == 'br':
                    x[0], y[0] = x[1], y[1]
                    y[1] += font_size*1.5
                elif block.name in ['strong', 'em', 's']:
                    x, y, rect = self.render(block, font_size, font_color, font_style + [block.name],
                                             [x, y], end_x, line_start_x, 0)
                    rects.append(rect)
                elif block.name == 'a':
                    x, y, rect = self.render(block, font_size, self.color_href, font_style,
                                             [x, y], end_x, line_start_x, 0)
                    rects.append(rect)
                    self.a_rects.append([rect, block.get('href')])
                elif block.name == 'code':
                    code_surface = self.render_code(font_size, font_style, block.contents[0])
                    if line_start_x == x[0]:
                        self.text_screen.blit(code_surface,(x[0], y[0]))
                        x[0] += code_surface.get_width()
                    else:
                        if x[0]+code_surface.get_width() < end_x:
                            self.text_screen.blit(code_surface, (x[0], y[0]))
                            x[0] += code_surface.get_width()
                        else:
                            x[0] = x[1]
                            y[0] += font_size*1.5
                            y[1] += font_size*1.5
                            self.text_screen.blit(code_surface, (x[0], y[0]))
                            x[0] += code_surface.get_width()
                else:
                    pass
            if block.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul',
                              'ol_nest', 'ul_nest', 'li', 'blockquote', 'hr']:
                label = eval('_html_label.' + block.name + '()')
                data = label.data
                self_font_size = data.calc_pos(label.font_size, font_size, self.font_normal_size)
                data.calc_style(self_font_size, self.font_normal_size)
                new_x = x[1] + data.margin_left
                new_y = y[1] + max(data.margin_top, last_margin_bottom)
                new_end_x = end_x - data.margin_right
                padding_start_x = new_x + data.border_left_width + data.padding_left
                padding_start_y = new_y + data.border_top_width + data.padding_top
                padding_end_x = new_end_x - data.border_right_width - data.padding_right
                content_height = 0
                if block.name != 'hr':
                    start_list = None
                    if block.name in ['ol', 'ol_nest']:
                        start_list = block.get('start')
                        if start_list is None:
                            start_list = 1
                        start_list = int(start_list)
                    _, y1, rect = self.render(block, self_font_size, font_color, font_style,
                                              [[padding_start_x, padding_start_x], [padding_start_y, padding_start_y]],
                                              padding_end_x, padding_start_x, 0, start_list)
                    rects.append(rect)
                    content_height = y1[1] - padding_start_y
                if block.name == 'li':
                    if list_start is None:
                        self.text_screen.blit(pygame.transform.smoothscale(pygame.image.load('circle.png'),(6,6)),
                                              (round(new_x - 12)-3, round(new_y + 1.5*self_font_size/2)-3))
                    else:
                        num = self.set_font(font_size, font_style).render(str(list_start)+'.', True, (0, 0, 0))
                        self.text_screen.blit(num, (round(new_x - 5)-num.get_width(), round(new_y + 1.5*self_font_size/2)-num.get_height()/2))
                        list_start += 1
                if '绘制边框和背景':
                    if not(data.background_color is None):
                        pygame.draw.rect(self.screen, data.background_color,
                                         (new_x, new_y, new_end_x-x[1],
                                          data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width))
                    if data.border_top_width > 0 and not (data.border_top_color is None):  # 上边框
                        pygame.draw.rect(self.screen, data.border_top_color, (new_x, new_y,
                                                                              new_end_x-x[1], data.border_top_width))
                    if data.border_left_width > 0 and not (data.border_left_color is None):  # 左边框
                        pygame.draw.rect(self.screen, data.border_left_color,
                                         (new_x, new_y,data.border_left_width,
                                          data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width))
                    if data.border_right_width > 0 and not (data.border_right_color is None):  # 右边框
                        pygame.draw.rect(self.screen, data.border_right_color,
                                         (new_end_x, new_y, data.border_right_width,
                                          data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width))
                    if data.border_bottom_width > 0 and not (data.border_bottom_color is None):  # 下边框
                        pygame.draw.rect(self.screen, data.border_bottom_color,
                                         (new_x, new_y + data.border_top_width + data.padding_top + content_height,
                                          new_end_x - x[1], data.border_bottom_width))
                y[1] = new_y + data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width
                if i == len(block_contents)-1:
                    y[1] += data.margin_bottom
                y[0] = y[1]
                last_margin_bottom = data.margin_bottom
        return x, y, rects

    def display(self, pygame_events, mouse_x, mouse_y, mouse_pressed):
        """
        显示 Markdown 渲染结果
        :param pygame_events: Pygame 事件列表
        :param mouse_x: 鼠标的 X 坐标
        :param mouse_y: 鼠标的 Y 坐标
        :param mouse_pressed: 鼠标是否按下的布尔值
        :return: None
        """
        # 背景绘制
        if self.background_rendering:
            # 使用反向的间距
            pygame.draw.rect(self.screen, self.color_area_background,
                             (self.x - self.margin,
                              self.y - self.margin,
                              self.w + (2 * self.margin),
                              self.h + (2 * self.margin)))

        # 设置起始位置（考虑滚动的偏移量）
        self.a_rects = []
        self.text_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.render(self.blocks, self.font_normal_size, (0, 0, 0), [],
                    [[self.x, self.x], [self.y, self.y]], self.x+self.w, self.x, 0)
        self.screen.blit(self.text_screen, (0, 0))
        # print(self.a_rects)
