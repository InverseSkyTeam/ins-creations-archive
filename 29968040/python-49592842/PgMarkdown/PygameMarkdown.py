from . import _html_label
from ._render_pre import PreCode
from ._table import Table
import pygame
import pygame.gfxdraw
import bs4
import copy
from .Load import Load, load


def make_circle(radius):
    surface = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
    pygame.draw.circle(surface, (63, 63, 63), (radius, radius), radius)
    return pygame.transform.smoothscale(surface, (6, 6))


class MarkdownRenderer:
    from ._render_code import render_code, render_code_to_screen, render_pre_code
    from ._font import set_font
    from ._render_inline_LaTeX import render_inline_LaTeX
    from ._render_other import render_br, return_line
    from ._render_txt import render_txt
    from ._scrollbar import scrollbarLength_contentScrollLength, contentScrollLength_scrollbarLength, render_scroll, handle_scroll
    from ._mouse import handle_url, handle_mouse_input

    def __init__(self):
        self.x: int = None
        self.y: int = None
        self.w: int = None
        self.h: int = None
        self.margin: int = None
        self.screen: pygame.Surface = None
        self.border_screen: pygame.Surface = None  # 用于存储边框、背景的画布
        self.text_screen: pygame.Surface = None  # 专门存储文字、图片的画布
        self.line_buffer: list = [[None, None, 0]]  # 行缓冲区，第一项存储该行起始位置
        self.img_url: dict = {}  # 用于存储图片链接
        self.in_line_LaTeX: dict = {}  # 内联公式缓存
        self.LaTeX: dict = {}  # 行间公式缓存
        self.render_height = 0  # 渲染区域总高度

        # 颜色
        self.color_area_background = (255, 255, 255)  # 背景颜色
        self.color_href = (0x34, 0x98, 0xdb)  # 超链接颜色
        self.color_href_hover = (0x14, 0x55, 0x8f)  # 超链接鼠标悬停颜色

        # 字体
        self.font_normal_size = 16  # 根节点字体大小
        self.font_normal_color = (63, 63, 63)  # 默认字体颜色
        self.fonts = [None for _ in range(50)]  # 为减少加载时间，加载的字体缓存到这里
        self.fonts_bold = [None for _ in range(50)]  # 粗体字体缓存

        # 滚动条
        self.scrollbar: pygame.Rect = None
        self.contentScrollLength = 0  # 内容滚动的距离
        self.scroll_color = (153, 153, 153)  # 滚动条颜色
        self.scroll_dragging = False  # 是否在拖动滚动条

        self.html = ""
        self.blocks = None
        self.background_rendering = True  # 是否渲染背景

        self.img_circle: pygame.Surface = make_circle(50)  # 无序列表前的圆点
        self.render_num = None  # 标记下次return_line时是否绘制列表圆点或序号
        self.render_queue_text_screen: list = []  # 渲染队列
        self.render_queue_border_screen: list = []  # 渲染队列

    def load_data(self, data):
        self.render_queue_text_screen: list = []  # 清空渲染队列
        self.render_queue_border_screen: list = []  # 清空渲染队列
        self.blocks = data.blocks
        self.html = data.html
        self.img_url = data.img_url
        self.in_line_LaTeX = data.in_line_LaTeX
        self.LaTeX = data.LaTeX

    def set_area(self, surface, offset_x, offset_y, width=-1, height=-1, margin=10) -> None:
        """
        设置 Markdown 渲染区域的位置和大小，并**预渲染**
        :param surface: 渲染到的 pygame Surface 对象
        :param offset_x: 相对于 Surface 左上角的 X 偏移量
        :param offset_y: 相对于 Surface 左上角的 Y 偏移量
        :param width: 渲染区域的宽度，默认为 -1，表示使用 Surface 的宽度
        :param height: 渲染区域的高度，默认为 -1，表示使用 Surface 的高度
        :param margin: 渲染区域与边界的间距，默认为 10
        :return: None
        """

        # 计算渲染区域
        self.margin = margin
        # 为了简化计算，将间距从初始的 x、y、w 和 h 中减去。
        # 在渲染背景矩形时，我们将间距添加回来。
        # 这样，间距对其他计算没有任何影响。
        self.x = offset_x + margin
        self.y = offset_y + margin
        # 如果没有给定值，我们将取 Surface 的边界作为限制。
        self.w = width - (2 * self.margin) if width > 0 else surface.get_width() - offset_x - (2 * self.margin)
        self.h = height - (2 * self.margin) if height > 0 else surface.get_height() - offset_y - (2 * self.margin)

        # 初始化
        self.screen = surface
        self.img_url = {}  # 清空图片缓存
        self.render_height = 0  # 初始化内容总高度
        self.render_queue_text_screen: list = []  # 清空渲染队列
        self.render_queue_border_screen: list = []  # 清空渲染队列
        self.line_buffer = [[None, None, 0]]  # 清空行缓冲
        self.border_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.text_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

        # 开始预渲染
        end_y = self.render(self.blocks, self.x, self.y, self.x + self.w, self.x,
                            self.font_normal_size, self.font_normal_color, [], 0)[1]
        last_line_height = self.return_line()  # 最后一行还没闭合，需要强制闭合
        end_y += last_line_height  # 计算闭合后的末尾 y 坐标
        self.render_height = end_y - self.y  # 计算总高度
        self.contentScrollLength = 0  # 初始化内容滚动的距离
        self.scroll_dragging = False  # 是否在拖动滚动条
        if self.render_height > self.h:  # 渲染区域太大，需要滚动条
            self.scrollbar: pygame.Rect = pygame.Rect(self.x+self.w, self.y, 5, self.w / self.render_height * self.w)
        else:
            self.scrollbar = None  # 不需要滚动条

    def render(self, blocks, start_x, start_y, end_x, line_start_x,
               font_size, font_color, font_style, last_margin_bottom, list_start=None,
               href=None):
        """
        最重要的部分：总渲染
        :param blocks: 当前需要渲染的 html 代码
        :param start_x: 当前行起始的 x 坐标
        :param start_y: 当前行起始的 y 坐标
        :param end_x: 结束 x 坐标
        :param line_start_x: 下一行起始的 x 坐标
        :param font_size: 渲染的字体大小（单位为 px ）
        :param font_color: 渲染的字体颜色
        :param font_style: 渲染的字体样式
        :param last_margin_bottom: 上一个标签的下边界
        :param list_start: 如果当前为列表项，存储列表起始序号
        :param is_href: 是否是超链接
        :param href: 对应的链接
        :return: 为最后一行闭合前的 x, y 坐标，具体意思视情况而定
        """
        block_contents = blocks.contents
        if len(block_contents) == 0:  # 空元素，直接返回
            return start_x, start_y
        while block_contents[-1] == '\n':  # 去除末尾的 \n
            block_contents.pop()
            if len(block_contents) == 0:  # 空元素，直接返回
                return start_x, start_y
        while block_contents[0] == '\n':  # 去除开头的 \n
            block_contents.pop(0)
            if len(block_contents) == 0:  # 空元素，直接返回
                return start_x, start_y
        if len(block_contents) == 0:  # 空元素，直接返回
            return start_x, start_y

        # 开始渲染
        x, y = start_x, start_y
        for i, block in enumerate(block_contents):  # 遍历内部的所有标签
            # 普通文字
            if isinstance(block, bs4.element.NavigableString):
                # 处理文字
                txt = block.string
                if txt == '\n':  # 遇到 \n 跳过
                    continue
                if i > 1 and blocks.contents[i - 1].name == 'br':  # 上一个标签是br
                    txt = txt[2:]  # 上一个标签为br，就要去掉前面因为 bs4 解析错误的换行

                # 把文字绘制进行缓冲区内
                x, y = self.render_txt(x, y, end_x, line_start_x, txt, font_size, font_color, font_style, href)

            # 内联标签和内联公式
            elif block.name in ['strong', 'em', 's', 'a', 'img', 'br', 'code'] or \
                    block.name == 'span' and block['class'] == ['math', 'inline']:
                if block.name == 'br':  # 需要强制换行
                    x, y = self.render_br(x, y, line_start_x)
                elif block.name in ['strong', 'em', 's', 'a']:  # 加样式类的标签
                    new_font_color = self.color_href if block.name == 'a' else font_color  # 是超链接要换颜色
                    new_href = block.get('href') if block.name == 'a' else href  # 获取链接
                    x, y = self.render(block, x, y, end_x, line_start_x, font_size, new_font_color,
                                       font_style + [block.name], 0, href=new_href)
                elif block.name == 'code':  # 内联代码块
                    x, y = self.render_code_to_screen(x, y, end_x, line_start_x, font_size, font_style, block)
                elif block.name == 'span':  # 内联latex公式
                    x, y = self.render_inline_LaTeX(x, y, end_x, line_start_x, font_size, block)
                elif block.name == 'img':  # 图片
                    pass
                else:
                    pass

            # 块级标签，行间公式，嵌套列表
            elif block.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'table',
                                'ol_nest', 'ul_nest', 'li', 'blockquote', 'hr', 'pre', 'span']:
                last_line_height = self.return_line()  # 强制闭合上一行
                x = line_start_x  # 重设 x 坐标
                y += last_line_height  # 更新 y 坐标
                self.line_buffer = [[None, None, 0]]  # 清空 line_buffer

                label = eval('_html_label.' + block.name + '()')  # 当前标签样式
                data = label.data  # 当前标签样式数据
                if blocks.name == 'li' and i == 0:  # 注意，这里用的是blocks.name，不是block.name
                    data.margin_top = (0, 'px')  # 列表里第一个块不渲染上边界

                self_font_size: int = data.convert_units(label.font_size, font_size, self.font_normal_size)  # 当前标签字体大小
                data.calc_style(self_font_size, self.font_normal_size)  # 计算样式
                padding_pos = data.calc_padding(x, y, end_x, last_margin_bottom)  # 计算 content 的坐标
                content_height = 0  # content 的高
                if block.name == 'li':  # 列表项
                    if list_start is None:  # 无序列表
                        self.render_num = self.img_circle
                    else:  # 有序列表的 list_start 是编号
                        self.render_num = self.set_font(font_size, font_style).render(str(list_start) + '.', True, (0, 0, 0))
                        list_start += 1  # 编号加一
                if block.name not in ['hr', 'pre', 'span', 'table']:  # 这不是分割线、多行代码块、表格、行间公式，直接绘制
                    start_list = None  # 默认无序列表的 None
                    if block.name in ['ol', 'ol_nest']:  # 有序列表
                        start_list = 1 if block.get('start') is None else int(block.get('start'))
                    add_style = ['strong'] if block.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] else []
                    y1 = self.render(block, padding_pos[0], padding_pos[1], padding_pos[2], padding_pos[0],
                                     self_font_size, font_color, font_style + add_style, 0, start_list)[1]  # 递归绘制标签的子节点
                    child_line_height = self.return_line()
                    self.line_buffer = [[None, None, 0]]
                    content_height = y1 + child_line_height - padding_pos[1]  # 计算 content 的高
                if block.name == 'pre':  # 多行代码块
                    pre_data = PreCode(block.contents[0].contents, self_font_size, data, padding_pos[2]-padding_pos[0]+data.padding_left+data.padding_right)
                    content_height = pre_data.height
                    self.render_queue_text_screen.append({
                        'name': 'pre',
                        'data': pre_data,
                        'pos': (padding_pos[0] - data.padding_left, padding_pos[1])
                    })
                if block.name == 'span':  # 行间公式
                    LaTeX_surface = self.LaTeX[str(block.contents[0])]
                    LaTeX_width, LaTeX_height = LaTeX_surface.get_width(), LaTeX_surface.get_height()
                    self.render_queue_text_screen.append({
                        'name': 'surface',
                        'surface': LaTeX_surface,
                        'pos': (line_start_x + ((end_x - line_start_x) - LaTeX_width)/2, y),
                        'href': None,
                        'hover': None
                    })
                    content_height = LaTeX_height
                if block.name == 'table':  # 表格
                    table_contents = []
                    for tbody in block.contents:
                        if tbody == '\n':
                            continue
                        for line in tbody.contents:
                            if line == '\n':
                                continue
                            table_contents.append([])
                            is_header = line['class'] == ['header']
                            for tblock in line.contents:
                                if tblock == '\n':
                                    continue
                                style = tblock.get('style')
                                last_queue_len = len(self.render_queue_text_screen)
                                _, y1 = self.render(tblock, 0, 0, 2147483647, 0, self_font_size, font_color,
                                                    font_style+(['strong'] if is_header else []), 0)
                                tblock_height = self.return_line() + y1  # 强制闭合上一行
                                self.line_buffer = [[None, None, 0]]  # 清空 line-buffer
                                tblock_sf = self.render_queue_text_screen[last_queue_len:]
                                if len(tblock_sf) == 0:
                                    tblock_width = 0
                                else:
                                    tblock_width = max([sf['pos'][0]+sf['surface'].get_width() for sf in tblock_sf])
                                table_contents[-1].append([tblock_width, tblock_height, tblock_sf, style])
                                self.render_queue_text_screen = self.render_queue_text_screen[:last_queue_len]
                    content_height = 0
                    for line in table_contents:
                        content_height += max([dd[1] for dd in line]) + 1 + 2*6
                    content_height += 1
                    self.render_queue_text_screen.append({
                        'name': 'table',
                        'data': Table(self_font_size, table_contents, padding_pos[2]-padding_pos[0], content_height),
                        'pos': (padding_pos[0], padding_pos[1]),
                        'href': None,
                        'hover': None
                    })

                self.render_queue_border_screen.append([data, x, y, end_x, content_height, last_margin_bottom])
                y = data.calc_border(y, content_height, last_margin_bottom)
                if i == len(block_contents)-1:  # 最后一块，需要把 margin 加上
                    y += data.margin_bottom
                last_margin_bottom = data.margin_bottom
        return x, y

    def render_to_screen(self, pygame_events, mouse_x, mouse_y, mouse_pressed):
        for i in self.render_queue_text_screen:
            if i['name'] == 'pre':
                x, y = i['pos'][0], i['pos'][1] - self.contentScrollLength
                i['data'].render(self.text_screen, x, y, pygame_events, mouse_x, mouse_y, self.y, self.h)
                continue
            if i['name'] == 'table':
                x, y = i['pos'][0], i['pos'][1] - self.contentScrollLength
                i['data'].render(self.text_screen, (x, y), pygame_events, mouse_x, mouse_y)
                continue
            x, y = i['pos'][0], i['pos'][1] - self.contentScrollLength
            if i['href'] and pygame.Rect(x, y, i['surface'].get_width(), i['surface'].get_height()).collidepoint(
                    (mouse_x, mouse_y)):
                self.text_screen.blit(i['hover'], (x, y))
                continue
            self.text_screen.blit(i['surface'], (x, y))
        for i in self.render_queue_border_screen:
            i[0].draw_border(self.border_screen, i[1], i[2] - self.contentScrollLength, i[3], i[4], i[5])

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
        self.border_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.text_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.render_to_screen(pygame_events, mouse_x, mouse_y, mouse_pressed)
        self.border_screen.blit(self.text_screen, (0, 0))
        self.screen.blit(self.border_screen.subsurface(pygame.Rect(self.x, self.y, self.w, self.h)), (self.x, self.y))
        self.render_scroll()
        self.handle_mouse_input(pygame_events, mouse_x, mouse_y, mouse_pressed)
