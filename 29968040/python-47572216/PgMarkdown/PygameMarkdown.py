import pygame
import re
import markdown2
import bs4
from . import _html_label
from . import _render

class MarkdownRenderer:
    def __init__(self):
        self.x: int = None
        self.y: int = None
        self.w: int = None
        self.h: int = None
        self.margin: int = None
        self.screen: pygame.Surface = None  # 用于存储边框、背景的画布
        self.text_screen: pygame.Surface = None  # 专门存储文字、图片的画布

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

        self.blocks = self.blocks.contents
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
        self.text_screen = pygame.Surface((surface.get_width(), surface.get_height()))

    def render_block(self, block, label, start_x, start_y, end_x, last_label_margin_bottom, font_father_size):
        data = label.data
        data.calc_style(font_father_size, self.font_normal_size)

        start_x += data.margin_left
        end_x -= (data.margin_right + data.border_right_width)
        start_y += max(last_label_margin_bottom, data.margin_top)

        if data.border_top_width > 0 and not (data.border_top_color is None):  # 上边框
            pygame.draw.line(self.screen, data.border_top_color,
                             (start_x, start_y+data.border_top_width/2),
                             (end_x, start_y+data.border_top_width/2), width=data.border_top_width)
        content_height = 0
        if block.name!='hr':
            padding_start_x = start_x + data.padding_left
            padding_end_x = end_x - data.padding_right
            padding_start_y = start_y + data.padding_top
            normal_font_size = self.font_normal_size * label.font_size[0]
            normal_font_size = round(normal_font_size)
            pos = _render.render_text(self.screen, block.contents, block.name,
                                       pygame.font.Font('HarmonyHeiTi.ttf', normal_font_size), normal_font_size,
                                       pygame.font.Font('HarmonyHeiTi.ttf', round(normal_font_size * 0.875)),
                                       round(normal_font_size * 0.875), (0, 0, 0),
                                       padding_start_x, padding_start_y, padding_end_x, padding_start_x, label.data.line_height)
            content_height = pos[1] + normal_font_size*label.data.line_height - padding_start_y
        #if content_height > 0:
        #    pygame.draw.rect(self.screen, (200, 200, 200), (padding_start_x, padding_start_y,
        #                                                    padding_end_x - padding_start_x, 100))
        if data.border_left_width > 0 and not (data.border_left_color is None):  # 左边框
            pygame.draw.line(self.screen, data.border_left_color,
                             (start_x + data.border_left_width/2, start_y),
                             (start_x + data.border_left_width/2, start_y + data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width),
                             width=data.border_left_width)
        if data.border_right_width > 0 and not (data.border_right_color is None):  # 右边框
            pygame.draw.line(self.screen, data.border_right_color,
                             (end_x + data.border_right_width/2, start_y),
                             (end_x + data.border_right_width/2, start_y + data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width),
                             width=data.border_right_width)
        if data.border_bottom_width > 0 and not (data.border_bottom_color is None):  # 下边框
            pygame.draw.line(self.screen, data.border_bottom_color,
                             (start_x, start_y + data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width/2),
                             (end_x, start_y + data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width/2),
                             width=data.border_bottom_width)
        return start_y + data.border_top_width + data.padding_top + content_height + data.padding_bottom + data.border_bottom_width, data.margin_bottom


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
        line_position_y = self.y
        last_label_margin_bottom = 0

        # 渲染 Markdown 块
        for i in self.blocks:
            if i == '\n': continue
            line_position_y, last_label_margin_bottom = self.render_block(i, eval('_html_label.'+i.name+'()'),
                                                                          self.x, line_position_y,
                                                                          self.x + self.w,
                                                                          last_label_margin_bottom,
                                                                          self.font_normal_size * eval('_html_label.'+i.name+'()').font_size[0])
