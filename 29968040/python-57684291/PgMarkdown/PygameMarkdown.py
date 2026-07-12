from . import _html_label
from ._render_pre import PreCode
from ._table import Table
from ._url import Url
from ._render_debug import render_debug_sf
import pygame
import pygame.gfxdraw
import bs4
import threading as thr
import random
import copy
from .util.scroll_bar import VScrollBar
from .util.font_manager import FontManager


def make_circle(radius):
    surface = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
    pygame.draw.circle(surface, (63, 63, 63), (radius, radius), radius)
    return pygame.transform.smoothscale(surface, (6, 6))


def clear_wrap(contents):
    while len(contents) and contents[-1] == '\n':  # 去末尾的 \n
        contents.pop()
    while len(contents) and contents[0] == '\n':  # 去开头的 \n
        contents.pop(0)
    if len(contents) == 0:  # 空元素，直接返回
        return None
    return contents


def get_label_type(block):
    if isinstance(block, bs4.element.NavigableString):
        return 'text'  # 文本

    if block.name in ['strong', 'em', 's', 'a', 'img', 'br', 'code', 'span']:
        return 'inline'  # 内联标签
    elif block.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'ol_nest', 'ul_nest', 'li', 'blockquote']:
        return 'block'  # 块级标签
    elif block.name in ['hr', 'pre', 'table']:
        return 'no-child-block'  # 没有子元素的块级标签
    else:
        return 'none'  # 未知标签


class MarkdownRenderer:
    from ._render_code import render_code, render_code_to_screen
    from ._render_pic import render_inline_LaTeX, render_img, render_LaTeX
    from ._render_other import render_br, return_line
    from ._render_txt import render_txt
    from ._mouse import handle_url, handle_mouse_input

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.content_width: int = None
        self.screen: pygame.Surface = None
        self.border_screen: pygame.Surface = None  # 用于存储边框、背景的画布
        self.text_screen: pygame.Surface = None  # 专门存储文字、图片的画布
        self.line_buffer: list = [[None, None]]  # 行缓冲区，第一项存储该行起始位置
        self.img_url: dict = {}  # 用于存储图片链接
        self.bilibili_video: dict = {}
        self.in_line_LaTeX: dict = {}  # 内联公式缓存
        self.LaTeX: dict = {}  # 行间公式缓存
        self.render_height = 0  # 渲染区域总高度
        self.debug = 0
        self.update_token = None

        # 颜色
        self.color_area_background = (255, 255, 255)  # 背景颜色
        self.color_href = (0x34, 0x98, 0xdb)  # 超链接颜色
        self.color_href_hover = (0x14, 0x55, 0x8f)  # 超链接鼠标悬停颜色

        # 字体
        self.font_normal_size = 16  # 根节点字体大小
        self.font_normal_color = (63, 63, 63)  # 默认字体颜色
        self.font = FontManager('HarmonyOS_Regular.ttf', 'HarmonyOS_Bold.ttf', 'CHSansSC.ttf')
        
        # 滚动条
        self.scroll = VScrollBar(self.rect)

        self.html = ""
        self.blocks = None
        
        self.img_circle: pygame.Surface = make_circle(50)  # 无序列表前的圆点
        self.render_num = None  # 标记下次return_line时是否绘制列表圆点或序号
        self.render_queue_text_screen: list = []  # 渲染队列
        self.render_queue_border_screen: list = []  # 渲染队列
        self.render_queue_text_screen_temp: list = []  # 渲染队列
        self.render_queue_border_screen_temp: list = []  # 渲染队列
        self.end_update = False  # 是否可以更新画面
        self.file_data = None
        self.scroll_data_cache = {}  # 滚动条数据缓存，防止重排后滚动条重置

    def load_data(self, data):
        self.file_data = data
        self.render_queue_text_screen: list = []  # 清空渲染队列
        self.render_queue_border_screen: list = []  # 清空渲染队列
        self.blocks = data.blocks
        self.html = data.html
        self.img_url = copy.copy(data.img_url)
        self.in_line_LaTeX = copy.copy(data.in_line_LaTeX)
        self.LaTeX = copy.copy(data.LaTeX)
        self.bilibili_video = copy.copy(data.bilibili_video)
        self.scroll_data_cache = {}

    def set_area(self, surface, rect, scroll_shade):
        """
        设置 Markdown 渲染区域的位置和大小，并进行重排
        :param surface: 渲染到的 pygame Surface 对象
        :param rect: 渲染区域在 surface 中的位置
        :param scroll_shade: True表明滚动条会遮挡内容，反之不会遮挡
        :return: None
        """
        if scroll_shade:
            self.content_width = rect.w
        else:
            self.content_width = rect.w - 5
        self.rect = rect
        self.screen = surface
        self.scroll.update_rect(rect)
        self.update()

    def update(self):  # 重排操作
        self.end_update = False
        # self.img_url = {}  # 清空图片缓存
        self.update_token = token = random.random()
        self.render_queue_text_screen: list = []  # 清空渲染队列
        self.render_queue_border_screen: list = []  # 清空渲染队列
        self.line_buffer = [[None, None]]  # 清空行缓冲
        self.border_screen = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.text_screen = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        sy = 0
        _, end_y, mg = self.render(self.blocks, 0, [sy], self.content_width, 0,
                                   self.font_normal_size, self.font_normal_color, [], 0)
        end_y += mg
        self.render_height = end_y - sy  # 计算总高度
        if token != self.update_token:
            return
        self.scroll.update_content_length(self.render_height)
        self.end_update = True
        self.render_queue_border_screen_temp = [x for x in self.render_queue_border_screen]
        self.render_queue_text_screen_temp = [x for x in self.render_queue_text_screen]

    def render_table(self, block, self_font_size, font_color, font_style):
        table_contents = []
        for tbody in block:
            if tbody == '\n':
                continue
            is_header = tbody.name == 'thead'
            style = font_style + (['strong'] if is_header else [])
            for line in tbody:
                if line == '\n':
                    continue
                table_contents.append([])
                for tblock in line:
                    if tblock == '\n':
                        continue
                    last_queue_len = len(self.render_queue_text_screen)
                    y1 = self.render(tblock, 0, [0], 2147483647, 0, self_font_size, font_color, style, 0)[1]
                    tblock_height = self.return_line() + y1  # 强制闭合上一行
                    self.line_buffer = [[None, None]]  # 清空 line-buffer
                    tblock_sf = self.render_queue_text_screen[last_queue_len:]
                    if len(tblock_sf) == 0:
                        tblock_width = 0
                    else:
                        tblock_width = max([sf['pos'][0] + sf['surface'].get_width() for sf in tblock_sf])
                    rect = pygame.Rect(0, 0, tblock_width, tblock_height)
                    table_contents[-1].append({'rect': rect, 'surface': tblock_sf, 'style': tblock.get('style')})
                    self.render_queue_text_screen = self.render_queue_text_screen[:last_queue_len]
        return table_contents

    def render(self, blocks, start_x, start_y, end_x, line_start_x,
               font_size, font_color, font_style, margin, list_start=None,
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
        :param margin: 上一个标签的边界
        :param list_start: 如果当前为列表项，存储列表起始序号
        :param is_href: 是否是超链接
        :param href: 对应的链接
        :return: 为最后一行闭合前的 x, y 坐标，具体意思视情况而定
        """
        block_contents = clear_wrap(blocks.contents)
        if block_contents is None:
            return start_x, start_y[0], 0
        can_add = True

        # 开始渲染
        x, y = start_x, start_y[0]
        for i, block in enumerate(block_contents):  # 遍历内部的所有标签
            block_type = get_label_type(block)
            # 普通文字
            if block_type == 'text':
                # 处理文字
                txt = block.string
                if txt == '\n':  # 遇到 \n 跳过
                    continue
                y += margin
                if can_add:
                    start_y[0] += margin
                    can_add = False
                margin = 0
                if i > 1 and block_contents[i - 1].name == 'br':  # 上一个标签是br
                    txt = txt[1:]  # 上一个标签为br，就要去掉前面因为 bs4 解析错误的换行

                # 把文字绘制进行缓冲区内
                x, y = self.render_txt(x, y, end_x, line_start_x, txt, font_size, font_color, font_style, href)

            # 内联标签和内联公式
            elif block_type == 'inline':
                y += margin
                if can_add:
                    start_y[0] += margin
                    can_add = False
                margin = 0
                if block.name == 'br':  # 需要强制换行
                    x, y = self.render_br(x, y, line_start_x)
                elif block.name in ['strong', 'em', 's', 'a']:  # 加样式类的标签
                    new_font_color = self.color_href if block.name == 'a' else font_color  # 是超链接要换颜色
                    new_href = Url(block.get('href')) if block.name == 'a' else href  # 获取链接
                    x, y, _ = self.render(block, x, [y], end_x, line_start_x, font_size, new_font_color,
                                          font_style + [block.name], margin, href=new_href)
                elif block.name == 'code':  # 内联代码块
                    x, y = self.render_code_to_screen(x, y, end_x, line_start_x, font_size, font_style, block)
                elif block.name == 'span':  # 内联latex公式
                    if block['class'] == ['math', 'inline']:
                        x, y = self.render_inline_LaTeX(x, y, end_x, line_start_x, font_size, block)
                    else:
                        x, y = self.render_LaTeX(x, y, end_x, line_start_x, font_size, block)
                elif block.name == 'img':  # 图片
                    x, y = self.render_img(x, y, end_x, line_start_x, font_size, block, href)
                else:
                    pass

            # 块级标签，行间公式，嵌套列表
            elif block_type == 'block':
                last_line_height = self.return_line()  # 强制闭合上一行
                x = line_start_x  # 重设 x 坐标
                y += last_line_height  # 更新 y 坐标
                self.line_buffer = [[None, None]]  # 清空 line_buffer

                label = eval('_html_label.' + block.name + '()')  # 当前标签样式
                data = label.data  # 当前标签样式数据

                self_font_size: int = data.convert_units(label.font_size, font_size, self.font_normal_size)  # 当前标签字体大小
                data.calc_style(self_font_size, self.font_normal_size)  # 计算样式
                content_sx, content_ex = data.calc_width(x, end_x)
                content_height = 0  # content 的高
                have_top_padding = have_bottom_padding = False
                margin = max(data.margin_top, margin)

                if data.padding_top + data.border_top_width > 0:
                    have_top_padding = True
                    y += margin
                    if can_add:
                        start_y[0] += margin
                        can_add = False
                    margin = 0
                if data.padding_bottom + data.border_bottom_width > 0:
                    have_bottom_padding = True

                if block.name == 'li':  # 列表项
                    if list_start is None:  # 无序列表
                        self.render_num = self.img_circle
                    else:  # 有序列表的 list_start 是编号
                        self.render_num = self.font.get_font(font_size, font_style).render(str(list_start) + '.', True, self.font_normal_color)
                        list_start += 1  # 编号加一
                start_list = None  # 默认无序列表的 None
                if block.name in ['ol', 'ol_nest']:  # 有序列表
                    start_list = 1 if block.get('start') is None else int(block.get('start'))
                add_style = ['strong'] if block.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] else []
                yy = [y + data.border_top_width + data.padding_top if have_top_padding else y]
                y_temp = yy[0]
                _, y1, margin = self.render(block, content_sx, yy, content_ex, content_sx, self_font_size, font_color, font_style + add_style, margin, start_list)  # 递归绘制标签的子节点
                child_line_height = self.return_line()
                self.line_buffer = [[None, None]]
                if have_top_padding:
                    yy[0] = y_temp
                content_height = y1 + child_line_height - yy[0]  # 计算 content 的高
                y += yy[0] - y_temp
                if can_add:
                    start_y[0] += yy[0] - y_temp
                    can_add = False

                if have_bottom_padding:
                    content_height += margin
                    margin = data.margin_bottom
                else:
                    margin = max(data.margin_bottom, margin)

                self.render_queue_border_screen.append([data, x, y, end_x, content_height])
                y = data.calc_border1(y, content_height)
            elif block_type == 'no-child-block':
                last_line_height = self.return_line()  # 强制闭合上一行
                x = line_start_x  # 重设 x 坐标
                y += last_line_height  # 更新 y 坐标
                self.line_buffer = [[None, None]]  # 清空 line_buffer

                label = eval('_html_label.' + block.name + '()')  # 当前标签样式
                data = label.data  # 当前标签样式数据

                self_font_size: int = data.convert_units(label.font_size, font_size, self.font_normal_size)  # 当前标签字体大小
                data.calc_style(self_font_size, self.font_normal_size)  # 计算样式
                content_sx, content_ex = data.calc_width(x, end_x)
                content_height = 0  # content 的高
                margin = max(data.margin_top, margin)

                y += margin
                if can_add:
                    start_y[0] += margin
                    can_add = False
                margin = 0

                if block.name == 'pre':  # 多行代码块
                    pre_data = PreCode(block.contents[0].contents, self_font_size, data, content_ex - content_sx + data.padding_left + data.padding_right)
                    content_height = pre_data.height
                    self.render_queue_text_screen.append({
                        'name': 'pre',
                        'data': pre_data,
                        'pos': (content_sx - data.padding_left, y + data.border_top_width)
                    })
                if block.name == 'table':  # 表格
                    table_contents = self.render_table(block, self_font_size, font_color, font_style)
                    content_height = 1
                    for line in table_contents:
                        content_height += max([dd['rect'].h for dd in line]) + 1 + 2 * 6
                    self.render_queue_text_screen.append({
                        'name': 'table',
                        'data': Table(self_font_size, table_contents, content_ex - content_sx, content_height),
                        'pos': (content_sx, y),
                        'href': None,
                        'hover': None
                    })
                margin = data.margin_bottom

                self.render_queue_border_screen.append([data, x, y, end_x, content_height])
                y = data.calc_border1(y, content_height)

        return x, y, margin

    def render_to_screen(self, pygame_events, mouse_pos, mouse_pressed):
        tps_num = 0
        token = None
        mouse_pos = (mouse_pos[0] - self.rect.x, mouse_pos[1]-self.rect.y)
        for i in self.render_queue_text_screen_temp:
            pos = i['pos'][0], i['pos'][1] - self.scroll.offset
            if i['name'] in ['pre', 'table']: continue
            if i['href'] and i['surface'].get_rect(topleft=pos).collidepoint(mouse_pos):
                token = i['href'].token
        for i in self.render_queue_text_screen_temp:
            x, y = i['pos'][0], i['pos'][1] - self.scroll.offset
            if i['name'] == 'pre':
                tps_num += 1
                if self.scroll_data_cache.get(tps_num) is not None:
                    i['data'].scroll.load(self.scroll_data_cache.get(tps_num))
                i['data'].render(self.text_screen, x, y, pygame_events, self.rect.h)
                self.scroll_data_cache[tps_num] = i['data'].scroll.save()
            elif i['name'] == 'table':
                tps_num += 1
                if self.scroll_data_cache.get(tps_num) is not None:
                    i['data'].scroll.load(self.scroll_data_cache.get(tps_num))
                i['data'].render(self.text_screen, x, y, pygame_events, *mouse_pos)
                self.scroll_data_cache[tps_num] = i['data'].scroll.save()
            elif i['href'] and i['href'].token == token:
                self.text_screen.blit(i['hover'], (x, y))
            else:
                self.text_screen.blit(i['surface'], (x, y))

        has_choose = 1
        debug_sf = None
        for num, i in enumerate(self.render_queue_border_screen_temp):
            is_choose = i[0].draw_border(self.border_screen, i[1], i[2] - self.scroll.offset, i[3], i[4], mouse_pos)
            if is_choose and has_choose and self.debug:
                has_choose = 0
                i[0].draw_debug_border(self.text_screen, i[1], i[2] - self.scroll.offset, i[3], i[4])
                content_width = i[3] - i[0].margin_right - i[1] - i[0].margin_left
                debug_sf = render_debug_sf(i[0], (content_width, i[4]), pygame.font.SysFont('SimHei', 12), 12, (0,) * 3)
        if has_choose and self.rect.collidepoint(mouse_pos) and self.debug:
            _html_label.Label.draw_alpha_rect(self.text_screen, (111, 168, 220, int(0.66*255)), self.text_screen.get_rect())
        if debug_sf is not None:
            self.text_screen.blit(debug_sf, debug_sf.get_rect(midtop=self.text_screen.get_rect().midtop))

    def display(self, _pygame_events, mouse_pos, mouse_pressed):
        """
        显示 Markdown 渲染结果
        :param pygame_events: Pygame 事件列表
        :param mouse_pos: 鼠标的坐标
        :param mouse_pressed: 鼠标是否按下的布尔值
        :return: None
        """
        def convert(event):
            _dict = copy.deepcopy(event.__dict__)
            _type = event.type
            if 'pos' in _dict and _type == pygame.MOUSEBUTTONDOWN:
                _dict['pos'] = _dict['pos'][0] - self.rect.x, _dict['pos'][1] - self.rect.y
            return pygame.event.Event(_type, _dict)
        pygame_events = [convert(event) for event in _pygame_events]
        if self.end_update and self.file_data.can_update:
            self.file_data.can_update = 0
            self.in_line_LaTeX = copy.copy(self.file_data.in_line_LaTeX)
            self.LaTeX = copy.copy(self.file_data.LaTeX)
            self.img_url = copy.copy(self.file_data.img_url)
            self.bilibili_video = copy.copy(self.file_data.bilibili_video)
            tt = thr.Thread(target=self.update, args=(), name="T2")
            tt.start()

        self.border_screen = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.text_screen = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.render_to_screen(pygame_events, mouse_pos, mouse_pressed)
        self.border_screen.blit(self.text_screen, (0, 0))
        self.screen.blit(self.border_screen, self.rect)
        self.scroll.render(self.screen)
        self.scroll.handle_event(_pygame_events)
        self.handle_mouse_input(pygame_events)
