from . import _html_label, markdown2, mdx_math
import markdown
import pygame
import pygame.gfxdraw
import bs4
import webbrowser as wb
import requests
import hashlib


def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    md5_value = md5_hash.hexdigest()
    return md5_value


def set_font(font_size, font_style):
    """
    设置渲染的字体
    :param font_size: 字体大小
    :param font_style: 字体的样式列表
    :return: 字体
    """
    if 'strong' in font_style:  # 粗体
        font = pygame.font.Font('HarmonyHeiTi Bold.ttf', round(font_size))
    else:  # 非粗体
        font = pygame.font.Font('HarmonyHeiTi Medium.ttf', round(font_size))
    if 'em' in font_style:  # 斜体
        font.set_italic(True)
    if 's' in font_style:  # 删除线
        font.set_strikethrough(True)
    return font


def get_latex_url(txt, is_inline):
    txt = txt.replace('\\', '%255C')
    url = 'https://latex.vimsky.com/test.image.latex.php?fmt=png&val={inline}%255Cdpi%257B150%257D%2520%255Csmall%2520{txt}&dl=0'.format(inline='%255Cinline%2520' if is_inline else '', txt=txt)
    file_name = str(is_inline) + '_' + calculate_md5(txt)+'.png'
    with open(file_name, 'wb') as f:
        f.write(requests.get(url).content)
    return pygame.image.load(file_name)


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


def render_code(font_normal_size: int, font_size: int, font_style: list, code: str):
    """
    绘制内联代码块
    :param font_normal_size: 根节点的字体（单位为 px ）
    :param font_size: 代码块父节点的字体（单位为 px ）
    :param font_style: 字体的样式（是否加粗、斜体等）
    :param code: 代码
    :return: 渲染后的画布
    """
    label = _html_label.code()
    data = label.data

    self_font_size: int = data.convert_units(label.font_size, font_size, font_normal_size)  # 代码块内字体大小
    data.calc_style(self_font_size, font_normal_size)  # 计算边框、背景等样式
    font = set_font(self_font_size, font_style)  # 设置字体

    code_surface = font.render(code, True, (0, 0, 0))
    sf_left = data.margin_left + data.border_left_width + data.padding_left
    sf_right = data.margin_right + data.border_right_width + data.padding_right
    sf_top = data.border_top_width + data.padding_top
    sf_bottom = data.padding_bottom + data.border_bottom_width
    sf_width = sf_left + code_surface.get_width() + sf_right - data.margin_right - data.margin_left
    surface = pygame.Surface((sf_left + code_surface.get_width() + sf_right,
                              sf_top + code_surface.get_height() + sf_bottom),
                             pygame.SRCALPHA)
    pygame.draw.rect(surface, data.background_color,
                     (data.margin_left, data.margin_top, sf_width,
                      data.padding_top + code_surface.get_height() + data.padding_bottom),
                     border_radius=2)
    pygame.draw.rect(surface, data.border_left_color,
                     (data.margin_left, data.margin_top, sf_width,
                      data.padding_top + code_surface.get_height() + data.padding_bottom),
                     width=data.border_left_width, border_radius=2)
    surface.blit(code_surface, (data.margin_left + data.border_left_width + data.padding_left,
                                data.border_top_width+data.padding_top))
    return surface


class MarkdownRenderer:
    def __init__(self):
        self.x: int = None
        self.y: int = None
        self.w: int = None
        self.h: int = None
        self.margin: int = None
        self.screen: pygame.Surface = None
        self.border_screen: pygame.Surface = None  # 用于存储边框、背景的画布
        self.text_screen: pygame.Surface = None  # 专门存储文字、图片的画布
        self.line_buffer: list = [[None, None]]  # 行缓冲区
        self.img_url: dict = {}  # 用于存储图片链接
        self.in_line_LaTeX: dict = {}  # 内联公式缓存
        self.LaTeX: dict = {}  # 普通公式缓存

        # 颜色
        self.color_area_background = (255, 255, 255)  # 背景颜色
        self.color_href = (0x34, 0x98, 0xdb)  # 超链接颜色
        self.color_href_hover = (0x14, 0x55, 0x8f)  # 超链接鼠标悬停颜色

        # 字体
        self.font_normal_size = 16  # 根节点字体大小

        # 滚动条
        self.scroll_y = 0

        self.html = ""
        self.blocks = None
        self.background_rendering = True  # 是否渲染背景
        self.a_rects: list = []  # 存储超链接的rect
        self.in_down = 0  # 鼠标是否持续按下
        # 无序列表前的圆点
        self.img_circle: pygame.Surface = pygame.transform.smoothscale(pygame.image.load('circle.png'), (6, 6))

    def set_markdown(self, mdfile_path):
        # 加载 md 文件并解析为 HTML
        with open(mdfile_path, "r", encoding='utf-8') as f:
            md_string = ''.join(list(f))
        self.set_markdown_from_string(md_string)

    def set_markdown_from_string(self, md_string):
        # 从字符串加载 md 代码并解析为 HTML
        if 0 and 'last':  # markdown2 库解析
            self.html = markdown2.markdown(md_string, extras=['fenced-code-blocks', 'strike',
                                                              'cuddled-lists', 'tables', 'tag-friendly'])
        if 1 and 'new':  # markdown 库解析
            extensions = ['codehilite', 'tables', 'fenced_code', mdx_math.MathExtension()]
            self.html = markdown.markdown(md_string, extensions=extensions)
        self.html = '<html><head></head><body>'+self.html.replace('&amp;', '&')+'</body></html>'
        self.blocks = None
        self.parse_markdown_file()

    def parse_markdown_file(self):
        # 解析 HTML 代码
        self.blocks = bs4.BeautifulSoup(self.html, 'lxml').body
        self.img_url = {}

        # 把嵌套列表改成内联标签
        li_tags = self.blocks.find_all('li')
        script_tags = self.blocks.find_all('script')

        for li in li_tags:
            ol_tags = li.find_all('ol')
            ul_tags = li.find_all('ul')
            for ol in ol_tags:
                ol.name = 'ol_nest'
            for ul in ul_tags:
                ul.name = 'ul_nest'
        for script in script_tags:
            if script['type'] == 'math/tex':
                gs = str(script.contents[0])
                self.in_line_LaTeX[gs] = get_latex_url(gs, True)
            else:
                gs = str(script.contents[0])
                self.LaTeX[gs] = get_latex_url(gs, False)

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
        self.screen = surface
        self.text_screen = pygame.Surface((surface.get_width(), surface.get_height()), pygame.SRCALPHA)

    def return_line(self):
        # 把行缓冲区里的东西绘制出来
        if len(self.line_buffer) <= 1:
            return 0
        x, y = self.line_buffer[0]  # line_buffer 的第一个元素是这一行的起始位置
        line_buffer = self.line_buffer[1:]
        line_height = max([i[1] for i in line_buffer])  # 最大行高
        for i, sf in enumerate(line_buffer):
            self.text_screen.blit(sf[0], [x, y + (line_height - sf[1])/2])
            x += sf[0].get_width()
        return line_height

    def render_txt(self, start_x, start_y, end_x, line_start_x, text, font_size: int, font_color, font_style):
        """
        绘制普通文字
        :param start_x: 当前行起始的 x 坐标
        :param start_y: 当前行起始的 y 坐标
        :param end_x: 结束 x 坐标
        :param line_start_x: 下一行起始的 x 坐标
        :param text: 渲染的文字
        :param font_size: 渲染的字体大小（单位为 px ）
        :param font_color: 渲染的字体颜色
        :param font_style: 渲染的字体样式
        :return: 渲染最后一行的结束 x 坐标, 渲染后最后一行的起始 y 坐标
        """
        font = set_font(font_size, font_style)
        text = text.replace('\n', ' ')
        line_height = font_size * 1.5

        current_line = ""
        x, y = start_x, start_y
        if start_x == line_start_x or (len(self.line_buffer)==0 or self.line_buffer[0][0] is None):
            self.line_buffer[0] = [start_x, start_y]  # 这个是这一行第一个块，强制初始化
        for word in text:
            temp_line = current_line + word if current_line != "" else word
            if font.size(temp_line)[0] > end_x - x:  # 再加新字符就要换行了
                # 把最后一块字符加入 line-buffer 里
                self.line_buffer.append([font.render(current_line, True, font_color), line_height])
                line_new_height = self.return_line()  # 绘制一整行
                x = line_start_x  # 重设 x 坐标
                y += line_new_height  # 更新 y 坐标
                self.line_buffer = [[x, y]]  # 清空行缓冲
                current_line = word
            else:
                current_line = temp_line
        # 在最后一块没有换行，直接加入行缓冲区内
        self.line_buffer.append([font.render(current_line, True, font_color), line_height])
        return x + self.line_buffer[-1][0].get_width(), y

    def render_pre_code(self, text, font_size, font_style, line_height, start_x, start_y):
        if text[-1] == '\n':
            text = text[:-1]
        text = text.split('\n')
        font = set_font(font_size, font_style)
        line_height *= font_size
        x, y = start_x, start_y
        # surface = pygame.Surface((end_x-start_x, self.h), pygame.SRCALPHA)

        for word in text:
            font_surface = font.render(word, True, (0, 0, 0))
            self.text_screen.blit(font_surface, (x, y + (line_height - font_surface.get_height()) / 2))
            y += line_height
        return x, y

    def render(self, blocks, start_x, start_y, end_x, line_start_x,
               font_size, font_color, font_style, last_margin_bottom, list_start = None):
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
        :return: 大致为结束 x, y坐标，具体意思视情况而定
        """
        block_contents = blocks.contents
        while block_contents[-1] == '\n':  # 去除末尾的 \n
            block_contents.pop()
        while block_contents[0] == '\n':  # 去除开头的 \n
            block_contents.pop(0)
        x, y = start_x, start_y
        for i, block in enumerate(block_contents):  # 遍历内部的所有标签
            if isinstance(block, bs4.element.NavigableString):  # 这个是普通文字
                txt = str(block)
                if txt == '\n':  # 遇到 \n 同样跳过
                    continue
                if i > 1 and blocks.contents[i - 1].name == 'br':  # 上一个标签是br
                    txt = txt[1:]  # 上一个标签为br，就要去掉前面因为 bs4 解析错误的换行
                x, y = self.render_txt(x, y, end_x, line_start_x, txt, font_size, font_color, font_style)
            elif block.name in ['strong', 'em', 's', 'a', 'img', 'br', 'code'] or block.name == 'script' and block['type'] == 'math/tex':  # 当绘制的是内联块时
                if block.name == 'br':  # 需要强制换行
                    last_line_height = self.return_line()  # 强制闭合上一行
                    x = line_start_x  # 重设 x 坐标
                    y += last_line_height  # 更新 y 坐标
                    self.line_buffer = [[x, y]]  # 清空 line-buffer
                elif block.name in ['strong', 'em', 's', 'a']:  # 加样式类的标签
                    new_font_color = font_color if block.name == 'a' else font_color
                    x, y = self.render(block, x, y, end_x, line_start_x, font_size, new_font_color,
                                       font_style + [block.name], 0)
                elif block.name == 'code':  # 内联代码块
                    code_surface = render_code(self.font_normal_size, font_size, font_style, block.contents[0])
                    csf_width, csf_height = code_surface.get_width(), code_surface.get_height()
                    if x != line_start_x and x + csf_width > end_x:  # 这个代码块不是这一行第一个字符，而且这个代码块宽度超长
                        last_line_height = self.return_line()  # 强制闭合上一行
                        x = line_start_x  # 重设 x 坐标
                        y += last_line_height  # 更新 y 坐标
                        self.line_buffer = [[x, y], [code_surface, font_size * 1.5]]  # 清空行缓冲
                    else:
                        if x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
                            self.line_buffer = [[x, y]]
                        self.line_buffer.append([code_surface, font_size * 1.5])
                    x += csf_width
                elif block.name == 'script':  # 内联latex公式
                    code_surface = self.in_line_LaTeX[str(block.contents[0])]
                    csf_width, csf_height = code_surface.get_width(), code_surface.get_height()
                    if x != line_start_x and x + csf_width > end_x:  # 这个代码块不是这一行第一个字符，而且这个代码块宽度超长
                        last_line_height = self.return_line()  # 强制闭合上一行
                        x = line_start_x  # 重设 x 坐标
                        y += last_line_height  # 更新 y 坐标
                        self.line_buffer = [[x, y], [code_surface, max(font_size * 1.5, csf_height)]]  # 清空行缓冲
                    else:
                        if x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
                            self.line_buffer = [[x, y]]
                        self.line_buffer.append([code_surface, max(font_size * 1.5, csf_height)])
                    x += csf_width
                elif block.name == 'img':  # 图片
                    pass
                else:
                    pass
            elif block.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul',
                                'ol_nest', 'ul_nest', 'li', 'blockquote', 'hr', 'pre', 'script']:
                last_line_height = self.return_line()  # 强制闭合上一行
                x = line_start_x  # 重设 x 坐标
                y += last_line_height  # 更新 y 坐标
                self.line_buffer = [[None, None]]

                label = eval('_html_label.' + block.name + '()')  # 当前标签数据类
                data = label.data  # 当前标签样式类
                if blocks.name == 'li' and i == 0:
                    data.margin_top = (0, 'px')  # 列表里第一个块不渲染上边界

                self_font_size: int = data.convert_units(label.font_size, font_size, self.font_normal_size)  # 当前标签字体大小
                data.calc_style(self_font_size, self.font_normal_size)  # 计算样式
                padding_pos = data.calc_padding(x, y, end_x, last_margin_bottom)  # 计算 content 的坐标

                # 先把 margin 计算出来
                new_x = x + data.margin_left
                new_y = y + max(data.margin_top, last_margin_bottom)

                content_height = 0  # content 的高
                if block.name not in ['hr', 'pre', 'script']:  # 这不是分割线和多行代码块，直接绘制
                    start_list = None
                    if block.name in ['ol', 'ol_nest']:
                        start_list = 1  # if block.get('start') is None else int(block.get('start'))
                    _, y1 = self.render(block, padding_pos[0], padding_pos[1], padding_pos[2], padding_pos[0],
                                        self_font_size, font_color, font_style, 0, start_list)  # 递归绘制标签的子节点
                    child_line_height = self.return_line()
                    self.line_buffer = [[None, None]]
                    content_height = y1 + child_line_height - padding_pos[1]  # 计算content的高
                if block.name == 'pre':  # 多行代码块
                    pre_data = _html_label.pre()
                    px, py = self.render_pre_code(block.contents[0].contents[0], font_size * pre_data.font_size[0],
                                                  font_style, 1.5, padding_pos[0], padding_pos[1])
                    content_height = py - padding_pos[1]
                if block.name == 'script':
                    code_surface = self.LaTeX[str(block.contents[0])]
                    csf_width, csf_height = code_surface.get_width(), code_surface.get_height()
                    self.text_screen.blit(code_surface, [line_start_x + ((end_x - line_start_x) - csf_width)/2, y])
                    content_height = csf_height
                if block.name == 'li':
                    if list_start is None:
                        self.text_screen.blit(self.img_circle,
                                              (round(new_x - 15), round(new_y + 1.5 * self_font_size / 2) - 3))
                    else:
                        num = set_font(font_size, font_style).render(str(list_start) + '.', True, (0, 0, 0))
                        self.text_screen.blit(num, (
                            (new_x - 5) - num.get_width(),
                            new_y + 1.5 * self_font_size / 2 - num.get_height() / 2 - 1))
                        list_start += 1
                y = data.draw_border(self.border_screen, x, y, end_x, content_height, last_margin_bottom)
                if i == len(block_contents)-1:
                    y += data.margin_bottom
                last_margin_bottom = data.margin_bottom
        return x, y

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

        self.a_rects = []
        self.border_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.text_screen = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        end_x, end_y = self.render(self.blocks, self.x, self.y, self.x+self.w, self.x,
                                   self.font_normal_size, (0, 0, 0), [], 0)
        last_line_height = self.return_line()
        end_x = self.x
        end_y += last_line_height
        self.screen.blit(self.border_screen, (0, 0))  # 把边框画布绘制到背景上
        self.screen.blit(self.text_screen, (0, 0))  # 把文字画布绘制到背景上
