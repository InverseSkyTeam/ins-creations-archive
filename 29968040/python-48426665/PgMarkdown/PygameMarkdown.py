from . import _html_label
from ._render_pre import PreCode
import pygame
import pygame.gfxdraw
import bs4
import time
import multiprocessing
import webbrowser as wb
import requests
import hashlib
from io import BytesIO
import urllib.parse
from .code_hlight import CodeHilite
import concurrent.futures
import pypandoc
extra = '-abbreviations+all_symbols_escapable-angle_brackets_escapable-autolink_bare_uris+backtick_code_blocks-blank_before_blockquote-blank_before_header-bracketed_spans-citations-compact_definition_lists-definition_lists-east_asian_line_breaks-emoji+escaped_line_breaks-example_lists-fancy_lists+fenced_code_attributes+fenced_code_blocks-fenced_divs-footnotes-four_space_rule-grid_tables-gutenberg-hard_line_breaks-header_attributes-ignore_line_breaks-implicit_figures-implicit_header_references-inline_code_attributes-inline_notes+intraword_underscores-latex_macros-line_blocks-link_attributes+lists_without_preceding_blankline-markdown_attribute-markdown_in_html_blocks-mmd_header_identifiers-mmd_link_attributes-mmd_title_block-multiline_tables-native_divs-native_spans-old_dashes-pandoc_title_block+pipe_tables-raw_attribute+raw_html-raw_tex-rebase_relative_paths-short_subsuperscripts-shortcut_reference_links-simple_tables+space_in_atx_header-spaced_reference_links+startnum+strikeout-subscript-superscript-table_captions-task_lists+tex_math_dollars-tex_math_double_backslash-tex_math_single_backslash-yaml_metadata_block'
pdoc_args = ['--from', 'markdown_strict'+extra, '--katex', '--no-highlight', '--columns=2147483647']


def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    md5_value = md5_hash.hexdigest()
    return md5_value


def get_latex_url(args):
    txt, is_inline = args
    txt = urllib.parse.quote(txt.replace('\r\n', '').replace('\n', ''))
    txt = urllib.parse.quote(txt)
    url = 'https://latex.vimsky.com/test.image.latex.php?' + \
          'fmt=png&val={inline}%255Cdpi%257B150%257D%2520%255Cfootnotesize%2520{txt}&dl=0'\
        .format(inline='%255Cinline%2520' if is_inline else '', txt=txt)
    file_data = requests.get(url).content
    return pygame.image.load_extended(BytesIO(file_data))


def get_latex_url_list(txt_list):
    if True:  # __name__ == "__main__":
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            results = executor.map(get_latex_url, txt_list)
        return results


def merge_surface(sf1: pygame.Surface, sf2: pygame.Surface):
    """
    垂直居中对齐合并画布
    :param sf1: 画布 1
    :param sf2: 画布 2
    :return: 合并后的画布
    """
    width1, height1 = sf1.get_width(), sf1.get_height()
    width2, height2 = sf2.get_width(), sf2.get_height()
    new_sf = pygame.Surface((width1+width2, max(height1, height2)), pygame.SRCALPHA)
    width3, height3 = new_sf.get_width(), new_sf.get_height()
    new_sf.blits(((sf1, (0, (height3 - height1) / 2)),
                  (sf2, (width1, (height3 - height2) / 2))))
    return new_sf


class MarkdownRenderer:
    from ._render_code import render_code, render_code_to_screen, render_pre_code
    from ._font import set_font
    from ._render_inline_LaTeX import render_inline_LaTeX
    from ._render_other import render_br, return_line
    from ._render_txt import render_txt
    from ._scrollbar import scrollbarLength_contentScrollLength, contentScrollLength_scrollbarLength, render_scroll, handle_mouse_scroll, handle_scroll
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
        self.line_buffer: list = [[None, None, 0]]  # 行缓冲区
        self.img_url: dict = {}  # 用于存储图片链接
        self.in_line_LaTeX: dict = {}  # 内联公式缓存
        self.LaTeX: dict = {}  # 普通公式缓存
        self.render_height = 0  # 渲染区域总高度

        # 颜色
        self.color_area_background = (255, 255, 255)  # 背景颜色
        self.color_href = (0x34, 0x98, 0xdb)  # 超链接颜色
        self.color_href_hover = (0x14, 0x55, 0x8f)  # 超链接鼠标悬停颜色

        # 字体
        self.font_normal_size = 16  # 根节点字体大小
        self.font_normal_color = (0, 0, 0)
        self.fonts = [None for _ in range(50)]
        self.fonts_bold = [None for _ in range(50)]

        # 滚动条
        self.scrollbar: pygame.Rect = None
        self.contentScrollLength = 0  # 内容滚动的距离
        self.scroll_color = (153, 153, 153)
        self.offest_y = None
        self.scroll_dragging = False  # 是否在拖动滚动条

        self.html = ""
        self.blocks = None
        self.background_rendering = True  # 是否渲染背景

        self.img_circle: pygame.Surface = pygame.transform.smoothscale(pygame.image.load('circle.png'), (6, 6))  # 无序列表前的圆点
        self.render_num = None  # 标记下次return_line时是否绘制列表圆点获序号
        self.render_queue_text_screen: list = []  # 渲染队列
        self.render_queue_border_screen: list = []  # 渲染队列

    def set_markdown(self, mdfile_path):
        # 加载 md 文件并解析为 HTML
        with open(mdfile_path, "r", encoding='utf-8') as f:
            md_string = ''.join(list(f))
        self.set_markdown_from_string(md_string)

    def set_markdown_from_string(self, md_string):
        # 从字符串加载 md 代码并解析为 HTML
        output = pypandoc.convert_text(md_string,
                                       to='html5',
                                       format='md',
                                       extra_args=pdoc_args,
                                       )
        self.html = output
        self.html = '<html><head></head><body>'+self.html+'</body></html>'
        self.blocks = None
        self.parse_markdown_file()

    def parse_markdown_file(self):
        time_s = time.time()
        # 解析 HTML 代码
        self.blocks = bs4.BeautifulSoup(self.html, 'lxml').body
        self.img_url = {}
        self.render_queue_text_screen: list = []  # 渲染队列
        self.render_queue_border_screen: list = []  # 渲染队列

        # 把嵌套列表改成内联标签
        li_tags = self.blocks.find_all('li')
        span_tags = self.blocks.find_all('span')
        pre_tags = self.blocks.find_all('pre')

        for li in li_tags:
            ol_tags = li.find_all('ol')
            ul_tags = li.find_all('ul')
            for ol in ol_tags:
                ol.name = 'ol_nest'
            for ul in ul_tags:
                ul.name = 'ul_nest'
        inline = []
        not_inline = []
        for span in span_tags:
            if span['class'] == ['math', 'inline']:
                gs = str(span.contents[0])
                if (gs, True) not in inline:
                    inline.append((gs, True))
                # self.in_line_LaTeX[gs] = get_latex_url(gs, True, self.in_line_LaTeX)
            else:
                gs = str(span.contents[0])
                if (gs, False) not in not_inline:
                    not_inline.append((gs, False))
                # self.LaTeX[gs] = get_latex_url((gs, False))
        res = get_latex_url_list(inline)
        res1 = get_latex_url_list(not_inline)
        for i, sf in enumerate(res):
            self.in_line_LaTeX[inline[i][0]] = sf
        for i, sf in enumerate(res1):
            self.LaTeX[not_inline[i][0]] = sf

        for pre in pre_tags:
            lang = pre.get('class')
            if lang is not None:
                lang = ' '.join(lang)
            else:
                pre.find('code').string += '\n'
                continue
            code = CodeHilite(src=pre.find('code').string, lang=lang)
            html = bs4.BeautifulSoup(code.hilite(), 'lxml')
            pre.find('code').replace_with(html.find('code'))

        # print(self.blocks)
        print("markdown解析完成，用时{}s".format(time.time()-time_s))

    def set_area(self, surface, offset_x, offset_y, width=-1, height=-1, margin=10) -> None:
        """
        设置 Markdown 渲染区域的位置和大小，并预渲染
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
        self.screen = surface

        self.img_url = {}
        self.render_height = 0  # 内容总高度
        self.render_queue_text_screen: list = []  # 清空渲染队列
        self.render_queue_border_screen: list = []  # 清空渲染队列
        self.line_buffer = [[None, None, 0]]
        self.border_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.text_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

        _, end_y = self.render(self.blocks, self.x, self.y, self.x + self.w, self.x,
                               self.font_normal_size, self.font_normal_color, [], 0)
        last_line_height = self.return_line()
        end_y += last_line_height

        self.render_height = end_y - self.y
        self.contentScrollLength = 0  # 内容滚动的距离
        self.scroll_dragging = False  # 是否在拖动滚动条
        if self.render_height > self.w:
            self.scrollbar: pygame.Rect = pygame.Rect(self.x+self.w, self.y, 5, self.w / self.render_height * self.w)
        else:
            self.scrollbar = None

    def render(self, blocks, start_x, start_y, end_x, line_start_x,
               font_size, font_color, font_style, last_margin_bottom, list_start=None,
               is_href=False, href=None):
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
        :param is_href: 是否是链接
        :param href: 对应的链接
        :return: 大致为结束 x, y坐标，具体意思视情况而定
        """
        block_contents = blocks.contents
        if len(block_contents) == 0:
            return start_x, start_y
        while block_contents[-1] == '\n':  # 去除末尾的 \n
            block_contents.pop()
        while block_contents[0] == '\n':  # 去除开头的 \n
            block_contents.pop(0)
        x, y = start_x, start_y
        for i, block in enumerate(block_contents):  # 遍历内部的所有标签
            if isinstance(block, bs4.element.NavigableString):  # 这个是普通文字
                txt = str(block)
                if txt == '\n':  # 遇到 \n 跳过
                    continue
                if i > 1 and blocks.contents[i - 1].name == 'br':  # 上一个标签是br
                    # 为什么解析时前面会出现两个换行？
                    txt = txt[2:]  # 上一个标签为br，就要去掉前面因为 bs4 解析错误的换行
                x, y = self.render_txt(x, y, end_x, line_start_x, txt, font_size, font_color, font_style, is_href, href)
            elif block.name in ['strong', 'em', 's', 'a', 'img', 'br', 'code'] or block.name == 'span' and block['class'] == ['math', 'inline']:  # 当绘制的是内联块时
                if block.name == 'br':  # 需要强制换行
                    x, y = self.render_br(x, y, line_start_x)
                elif block.name in ['strong', 'em', 's', 'a']:  # 加样式类的标签
                    new_font_color = self.color_href if block.name == 'a' else font_color
                    new_href = block.get('href') if block.name == 'a' else href
                    x, y = self.render(block, x, y, end_x, line_start_x, font_size, new_font_color,
                                       font_style + [block.name], 0, is_href=(block.name == 'a'), href=new_href)
                elif block.name == 'code':  # 内联代码块
                    x, y = self.render_code_to_screen(x, y, end_x, line_start_x, font_size, font_style, block)
                elif block.name == 'span':  # 内联latex公式
                    x, y = self.render_inline_LaTeX(x, y, end_x, line_start_x, font_size, block)
                elif block.name == 'img':  # 图片
                    pass
                else:
                    pass
            elif block.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul',
                                'ol_nest', 'ul_nest', 'li', 'blockquote', 'hr', 'pre', 'span']:
                last_line_height = self.return_line()  # 强制闭合上一行
                x = line_start_x  # 重设 x 坐标
                y += last_line_height  # 更新 y 坐标
                self.line_buffer = [[None, None, 0]]

                label = eval('_html_label.' + block.name + '()')  # 当前标签数据类
                data = label.data  # 当前标签样式类
                if blocks.name == 'li' and i == 0:  # 注意，这里用的是blocks.name，不是block.name
                    data.margin_top = (0, 'px')  # 列表里第一个块不渲染上边界

                self_font_size: int = data.convert_units(label.font_size, font_size, self.font_normal_size)  # 当前标签字体大小
                data.calc_style(self_font_size, self.font_normal_size)  # 计算样式
                padding_pos = data.calc_padding(x, y, end_x, last_margin_bottom)  # 计算 content 的坐标
                content_height = 0  # content 的高
                if block.name == 'li':
                    if list_start is None:
                        self.render_num = self.img_circle
                    else:
                        self.render_num = self.set_font(font_size, font_style).render(str(list_start) + '.', True, (0, 0, 0))
                        list_start += 1
                if block.name not in ['hr', 'pre', 'span']:  # 这不是分割线和多行代码块，直接绘制
                    start_list = None
                    if block.name in ['ol', 'ol_nest']:
                        start_list = 1 if block.get('start') is None else int(block.get('start'))
                    _, y1 = self.render(block, padding_pos[0], padding_pos[1], padding_pos[2], padding_pos[0],
                                        self_font_size, font_color, font_style, 0, start_list)  # 递归绘制标签的子节点
                    child_line_height = self.return_line()
                    self.line_buffer = [[None, None, 0]]
                    content_height = y1 + child_line_height - padding_pos[1]  # 计算content的高
                if block.name == 'pre':  # 多行代码块
                    pre_data = PreCode(block.contents[0].contents, self_font_size, data, padding_pos[2]-padding_pos[0]+data.padding_left+data.padding_right)
                    content_height = pre_data.height
                    self.render_queue_text_screen.append(['pre', pre_data, padding_pos[0] - data.padding_left, padding_pos[1]])
                if block.name == 'span':
                    LaTeX_surface = self.LaTeX[str(block.contents[0])]
                    LaTeX_width, LaTeX_height = LaTeX_surface.get_width(), LaTeX_surface.get_height()
                    # self.text_screen.blit(LaTeX_surface, [line_start_x + ((end_x - line_start_x) - LaTeX_width)/2, y])
                    self.render_queue_text_screen.append([LaTeX_surface, (line_start_x + ((end_x - line_start_x) - LaTeX_width)/2, y), None])
                    content_height = LaTeX_height
                # y = data.draw_border(self.border_screen, x, y, end_x, content_height, last_margin_bottom)
                self.render_queue_border_screen.append([data, x, y, end_x, content_height, last_margin_bottom])
                y = data.calc_border(y, content_height, last_margin_bottom)
                if i == len(block_contents)-1:
                    y += data.margin_bottom
                last_margin_bottom = data.margin_bottom
        return x, y

    def render_to_screen(self, pygame_events, mouse_x, mouse_y, mouse_pressed):
        for i in self.render_queue_text_screen:
            if i[0] == 'pre':
                x, y = i[2], i[3] - self.contentScrollLength
                i[1].render(self.text_screen, x, y, pygame_events, mouse_x, mouse_y, mouse_pressed, self.y, self.h)
                continue
            x, y = i[1][0], i[1][1] - self.contentScrollLength
            if i[2] and pygame.Rect(x, y, i[0].get_width(), i[0].get_height()).collidepoint(
                    (mouse_x, mouse_y)):
                self.text_screen.blit(i[3], (x, y))
                continue
            self.text_screen.blit(i[0], (x, y))
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
