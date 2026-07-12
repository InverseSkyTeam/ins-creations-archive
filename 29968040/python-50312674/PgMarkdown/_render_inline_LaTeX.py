import pygame
from ._url import Url
from PIL import Image, ImageFilter
video_state = pygame.transform.smoothscale(pygame.image.load('video_state.png'), (100, 100))
video_state.set_alpha(int(255 * 0.6))


def render_inline_LaTeX(self, x, y, end_x, line_start_x, font_size, block):
    """
    把内联LaTeX绘制到 screen(line-buffer) 里
    :param self: MarkdownRenderer类
    :param x: 当前行起始的 x 坐标
    :param y: 当前行起始的 y 坐标
    :param end_x: 结束 x 坐标
    :param line_start_x: 下一行起始的 x 坐标
    :param font_size: 代码块父节点的字体（单位为 px ）
    :param block: 当前的标签数据
    :return: 渲染完成后的x,y
    """
    LaTeX_surface = self.in_line_LaTeX[str(block.contents[0])]  # 获取已经预加载的公式图片
    if font_size / self.font_normal_size != 1:  # 当前字体大小不是正常大小
        LaTeX_width, LaTeX_height = LaTeX_surface.get_width(), LaTeX_surface.get_height()
        LaTeX_surface = pygame.transform.smoothscale(LaTeX_surface,
                                                     (round(LaTeX_width * font_size / self.font_normal_size),
                                                      round(LaTeX_height * font_size / self.font_normal_size)))
    LaTeX_width, LaTeX_height = LaTeX_surface.get_width(), LaTeX_surface.get_height()
    if x != line_start_x and x + LaTeX_width > end_x:  # 这个代码块不是这一行第一个字符，而且这个代码块宽度超长
        last_line_height = self.return_line()  # 强制闭合上一行
        x = line_start_x  # 重设 x 坐标
        y += last_line_height  # 更新 y 坐标
        self.line_buffer = [
            [x, y],
            {
                'name': 'LaTeX',
                'surface': LaTeX_surface,
                'height': max(font_size * 1.5, LaTeX_height),
                'href': None,
                'hover': None
            }
        ]
    else:
        if x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
            self.line_buffer = [[x, y]]
        self.line_buffer.append({
            'name': 'LaTeX',
            'surface': LaTeX_surface,
            'height': max(font_size * 1.5, LaTeX_height),
            'href': None,
            'hover': None
        })
    x += LaTeX_width
    return x, y


def scale_img(img, width):
    # 由于浮点数精度，目标宽高比不能直接看做 1.6
    height = width // 1.6
    aspect_ratio = img.get_width() / img.get_height()
    target_ratio = width / height
    if aspect_ratio > target_ratio:
        new_height = height
        new_width = int(height * aspect_ratio) + 1
    else:
        new_width = width
        new_height = int(width / aspect_ratio) + 1
    resized_img = pygame.transform.smoothscale(img, (new_width, new_height))
    x_offset = (new_width - width) // 2
    y_offset = (new_height - height) // 2
    result_img = resized_img.subsurface((x_offset, y_offset, width, height))
    result_img = pygame.transform.smoothscale(result_img, (width * 1.1, height * 1.1))
    return result_img.subsurface((int(width * 0.05), int(height * 0.05), width, height))


def blue_img(sf):
    pygame.image.save(sf, 'temp.png')
    pil_image = Image.open('temp.png')
    img1 = pil_image.filter(ImageFilter.GaussianBlur(radius=5))
    res = pygame.image.fromstring(img1.tobytes(), img1.size, img1.mode)
    mask = pygame.Surface(res.get_size(), pygame.SRCALPHA)
    mask.fill((0, 0, 0, int(255*0.2)))
    res.blit(mask, (0, 0))
    return res


def render_video_t(video_t):
    font = pygame.font.Font('HarmonyOS_Sans_SC_Regular.ttf', 14)
    sf = pygame.Surface((58, 24), pygame.SRCALPHA)
    pygame.draw.rect(sf, (0, 0, 0, 255//2), (0, 0, 58, 24), border_radius=4)
    font_sf = font.render(video_t, True, (255, )*3)
    sf.blit(font_sf, ((sf.get_width()-font_sf.get_width())//2+1, (sf.get_height()-font_sf.get_height())//2+1))
    return sf


def _render_title(title):
    font = pygame.font.Font('HarmonyOS_Sans_SC_Regular.ttf', 16)
    if font.size(title)[0] < 260:
        return font.render(title, True, (255,) * 3)
    end = font.size('...')[0]
    current_line = ""
    for word in title:
        temp_line = current_line + word if current_line != "" else word  # 加入一个新字符
        if font.size(temp_line)[0] + end > 260:
            return font.render(current_line + '...', True, (255,) * 3)
        else:
            current_line = temp_line
    return font.render(current_line + '...', True, (255,) * 3)


def render_title(title, height):
    sf = _render_title(title)
    sf_width, sf_height = sf.get_size()
    sf_width *= height / 300
    sf_height *= height / 300
    return pygame.transform.smoothscale(sf, (round(sf_width), round(sf_height)))


def render_img(self, x, y, end_x, line_start_x, font_size, block, href):
    """
    把内联LaTeX绘制到 screen(line-buffer) 里
    :param self: MarkdownRenderer类
    :param x: 当前行起始的 x 坐标
    :param y: 当前行起始的 y 坐标
    :param end_x: 结束 x 坐标
    :param line_start_x: 下一行起始的 x 坐标
    :param font_size: 代码块父节点的字体（单位为 px ）
    :param block: 当前的标签数据
    :param href: 图片的链接
    :return: 渲染完成后的x,y
    """
    if block['src'].startswith('bilibili:'):
        video_data = self.bilibili_video[block['src']]
        if video_data is None:
            return x, y
        last_line_height = self.return_line()  # 强制闭合上一行
        x = line_start_x  # 重设 x 坐标
        y += last_line_height  # 更新 y 坐标
        img_surface = scale_img(video_data['cover_img'], end_x - line_start_x)
        img_width, img_height = img_surface.get_width(), img_surface.get_height()
        img_surface = blue_img(img_surface)
        img_surface.blit(render_video_t(video_data['t']), (20, img_height-29-24))
        img_surface.blit(render_title(video_data['title'], img_height), (20, 40))
        img_surface.blit(video_state, (img_width - 10 - 100, img_height - 24 - 84 + 10))
        self.line_buffer = [
            [x, y],
            {
                'name': 'img',
                'surface': img_surface,
                'height': max(font_size * 1.5, img_height),
                'img_height': img_height,
                'href': Url(video_data['url']),
                'hover': img_surface
            }
        ]
        last_line_height = self.return_line()  # 强制闭合上一行
        x = line_start_x  # 重设 x 坐标
        y += last_line_height  # 更新 y 坐标
        self.line_buffer = [[x, y]]
        return x, y

    img_surface = self.img_url[block['src']]  # 获取已经预加载的公式图片
    img_width, img_height = img_surface.get_width(), img_surface.get_height()
    bottom_height = font_size * 6 / 16  # 正常字体大小下，且 line-height 为 1.5 时，基线到底部的高度为 6 px

    if img_width > end_x - line_start_x:
        bottom_height = font_size * 4 / 16
        scale_num = (end_x - line_start_x) / img_width
        img_width = round(img_width * scale_num)
        img_height = round(img_height * scale_num)
        img_surface = pygame.transform.smoothscale(img_surface, (img_width, img_height))

    if x != line_start_x and x + img_width > end_x:  # 这个代码块不是这一行第一个字符，而且这个代码块宽度超长
        last_line_height = self.return_line()  # 强制闭合上一行
        x = line_start_x  # 重设 x 坐标
        y += last_line_height  # 更新 y 坐标
        self.line_buffer = [
            [x, y],
            {
                'name': 'img',
                'surface': img_surface,
                'height': max(font_size * 1.5, img_height + bottom_height),
                'img_height': img_height + bottom_height,
                'href': href,
                'hover': img_surface
            }
        ]
    else:
        if x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
            self.line_buffer = [[x, y]]
        self.line_buffer.append({
            'name': 'img',
            'surface': img_surface,
            'height': max(font_size * 1.5, img_height + bottom_height),
            'img_height': img_height + bottom_height,
            'href': href,
            'hover': img_surface
        })
    x += img_width
    return x, y
