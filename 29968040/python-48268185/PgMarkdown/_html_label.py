# 存储每个html标签的信息
# h1, h2, h3, h4, h5, h6, code, blockquote, p, ul, ul_nest, ol, ol_nest, pre, hr
import pygame
import tkinter as tk


root = tk.Tk()
screen_dpi = root.winfo_fpixels('1i')  # 返回每英寸像素数
root.destroy()


class Label:
    # 用于存储标签的属性
    def __init__(self):
        # 其他
        self.background_color = None

        # padding
        self.padding_top = (0, 'px')
        self.padding_right = (0, 'px')
        self.padding_bottom = (0, 'px')
        self.padding_left = (0, 'px')

        # margin
        self.margin_top = (0, 'px')
        self.margin_right = (0, 'px')
        self.margin_bottom = (0, 'px')
        self.margin_left = (0, 'px')

        # border
        self.border_top_width = (0, 'px')
        self.border_right_width = (0, 'px')
        self.border_bottom_width = (0, 'px')
        self.border_left_width = (0, 'px')
        self.border_top_color = None
        self.border_right_color = None
        self.border_bottom_color = None
        self.border_left_color = None

    def set_border(self, width, color):
        # 设置边框
        self.border_top_width = width
        self.border_right_width = width
        self.border_bottom_width = width
        self.border_left_width = width
        self.border_top_color = color
        self.border_right_color = color
        self.border_bottom_color = color
        self.border_left_color = color

    def set_margin(self, a, b=None, c=None, d=None):
        # 设置 margin
        if b is None:
            self.margin_top = a
            self.margin_right = a
            self.margin_bottom = a
            self.margin_left = a
        elif c is None:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = a
            self.margin_left = b
        elif d is None:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = c
            self.margin_left = b
        else:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = c
            self.margin_left = d

    def set_padding(self, a, b=None, c=None, d=None):
        # 设置 padding
        if b is None:
            self.padding_top = a
            self.padding_right = a
            self.padding_bottom = a
            self.padding_left = a
        elif c is None:
            self.padding_top = a
            self.padding_right = b
            self.padding_bottom = a
            self.padding_left = b
        elif d is None:
            self.margin_top = a
            self.margin_right = b
            self.margin_bottom = c
            self.margin_left = b
        else:
            self.padding_top = a
            self.padding_right = b
            self.padding_bottom = c
            self.padding_left = d

    @staticmethod
    def convert_units(pos: tuple, font_father_size: int, font_normal_size: int):
        """
        坐标单位转换
        :param pos: 要计算的单位
        :param font_father_size: 父节点的字体大小（必须以 px 为单位）
        :param font_normal_size: 根节点的字体大小（必须以 px 为单位）
        :return: 转换后的单位（单位为 px ）
        """
        unit = pos[1].lower()  # 单位
        if unit == 'px':
            return pos[0]
        elif unit == 'em':
            return pos[0] * font_father_size
        elif unit == 'rem':
            return pos[0] * font_normal_size
        elif unit == 'ex':  # 通常情况下，x的渲染高度为字体大小的4/5
            return pos[0] * font_father_size * 4 / 5
        elif unit == 'ch':  # 通常情况下，0的渲染宽度为字体大小*0.5864（这是谷歌的渲染结果）
            return pos[0] * font_father_size * 0.5864
        elif unit == 'in':
            return pos[0] * screen_dpi
        elif unit == 'cm':
            return pos[0] * screen_dpi / 2.54
        elif unit == 'mm':
            return pos[0] * screen_dpi / 25.4
        elif unit == 'pt':
            return pos[0] * screen_dpi / 72
        elif unit == 'pc':
            return pos[0] * screen_dpi / 6

    def calc_style(self, font_father_size, font_normal_size):
        """
        计算 css 样式
        :param font_father_size: 父节点的字体大小（必须以 px 为单位）
        :param font_normal_size: 根节点的字体大小（必须以 px 为单位）
        :return: None
        """
        # padding
        self.padding_top = self.convert_units(self.padding_top, font_father_size, font_normal_size)
        self.padding_right = self.convert_units(self.padding_right, font_father_size, font_normal_size)
        self.padding_bottom = self.convert_units(self.padding_bottom, font_father_size, font_normal_size)
        self.padding_left = self.convert_units(self.padding_left, font_father_size, font_normal_size)

        # margin
        self.margin_top = self.convert_units(self.margin_top, font_father_size, font_normal_size)
        self.margin_right = self.convert_units(self.margin_right, font_father_size, font_normal_size)
        self.margin_bottom = self.convert_units(self.margin_bottom, font_father_size, font_normal_size)
        self.margin_left = self.convert_units(self.margin_left, font_father_size, font_normal_size)

        # border
        self.border_top_width = self.convert_units(self.border_top_width, font_father_size, font_normal_size)
        self.border_right_width = self.convert_units(self.border_right_width, font_father_size, font_normal_size)
        self.border_bottom_width = self.convert_units(self.border_bottom_width, font_father_size, font_normal_size)
        self.border_left_width = self.convert_units(self.border_left_width, font_father_size, font_normal_size)

    def calc_padding(self, x, y, end_x, last_margin_bottom):
        # 计算 content 的位置
        x += self.margin_left
        y += max(self.margin_top, last_margin_bottom)
        end_x -= self.margin_right
        return (x + self.border_left_width + self.padding_left,
                y + self.border_top_width + self.padding_top,
                end_x - self.border_right_width - self.padding_right)

    def draw_border(self, screen, x, y, end_x, content_height, last_margin_bottom):
        # 绘制边框和背景
        x += self.margin_left
        y += max(last_margin_bottom, self.margin_top)
        end_x -= self.margin_right

        border_width = end_x - x
        border_height = self.border_top_width + self.padding_top + content_height + self.padding_bottom + self.border_bottom_width

        if not (self.background_color is None):
            pygame.draw.rect(screen, self.background_color, (x, y, border_width, border_height))
        if self.border_top_width > 0 and not (self.border_top_color is None):  # 上边框
            pygame.draw.rect(screen, self.border_top_color, (x, y, border_width, self.border_top_width))
        if self.border_left_width > 0 and not (self.border_left_color is None):  # 左边框
            pygame.draw.rect(screen, self.border_left_color, (x, y, self.border_left_width, border_height))
        if self.border_right_width > 0 and not (self.border_right_color is None):  # 右边框
            pygame.draw.rect(screen, self.border_right_color, (end_x - self.border_right_width, y,
                                                               self.border_right_width, border_height))
        if self.border_bottom_width > 0 and not (self.border_bottom_color is None):  # 下边框
            pygame.draw.rect(screen, self.border_bottom_color, (x, y + border_height - self.border_bottom_width,
                                                                border_width, self.border_bottom_width))
        return y + border_height


class h1:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # border
        self.data.border_bottom_width = (1, 'px')
        self.data.border_bottom_color = (238, 238, 238)

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # padding
        self.data.padding_bottom = (0.2, 'em')

        # font-size
        self.font_size = (2, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h2:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # border
        self.data.border_bottom_width = (1, 'px')
        self.data.border_bottom_color = (238, 238, 238)

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # padding
        self.data.padding_bottom = (0.2, 'em')

        # font-size
        self.font_size = (1.5, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h3:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (1.17, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h4:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (1, 'em')  # 或(16, 'px')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h5:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (0.83, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class h6:
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0.5, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (0.67, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class code:
    # 内联代码块
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0, 'px'), (0.2, 'em'))

        # padding
        self.data.set_padding((0.1, 'em'),(0.2, 'em'))

        # border
        self.data.set_border((1, 'px'), (232, 232, 232))

        # background-color
        self.data.background_color = (0xfa, 0xfa, 0xfa)

        # font-size
        self.font_size = (0.875, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class blockquote:
    # 区块引用
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((0, 'px'), (0, 'px'), (20, 'px'))

        # padding
        self.data.set_padding((10, 'px'),(20, 'px'))

        # border
        self.data.border_left_width = (5, 'px')
        self.data.border_left_color = (238, 238, 238)

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class p:
    # 段落
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'rem'), (0, 'px'))

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ul:
    # 无序列表
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'rem'), (0, 'px'))

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ul_nest:
    # 嵌套无序列表（嵌套列表没有margin，某种意义上属于内联原素）
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ol:
    # 有序列表
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'rem'), (0, 'px'))

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class ol_nest:
    # 嵌套有序列表（嵌套列表没有margin，某种意义上属于内联原素）
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # padding
        self.data.padding_left = (1.5, 'em')

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class pre:
    # 多行代码块
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # padding
        self.data.set_padding((1, 'em'))

        # border
        self.data.set_border((1, 'px'), (232, 232, 232))

        # background-color
        self.data.background_color = (0xfa, 0xfa, 0xfa)

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class hr:
    # 分割线
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # margin
        self.data.set_margin((1, 'em'), (0, 'px'))

        # border
        self.data.border_bottom_width = (1, 'px')
        self.data.border_bottom_color = (238, 238, 238)

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0)


class li:
    # 列表项
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)


class script:
    # 列表项
    # background_color, padding, border, margin
    def __init__(self):
        self.data = Label()

        # font-size
        self.font_size = (1, 'em')

        # color
        self.color = (0, 0, 0, 255 * 0.75)

