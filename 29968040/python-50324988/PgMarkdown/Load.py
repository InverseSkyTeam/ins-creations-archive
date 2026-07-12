import re
# import pypandoc
from .code_hlight import CodeHilite
import time
import bs4
import concurrent.futures
from io import BytesIO
import urllib.parse
import requests
import pygame
import hashlib
import os
import threading as thr


extra = [
    '-abbreviations',
    '+all_symbols_escapable',
    '-angle_brackets_escapable',
    '-autolink_bare_uris',
    '+backtick_code_blocks',
    '-blank_before_blockquote',
    '-blank_before_header'
    '-bracketed_spans',
    '-citations',
    '-compact_definition_lists',
    '-definition_lists',
    '-east_asian_line_breaks',
    '-emoji',
    '+escaped_line_breaks',
    '-example_lists',
    '-fancy_lists',
    '+fenced_code_attributes',
    '+fenced_code_blocks',
    '-fenced_divs',
    '-footnotes',
    '-four_space_rule',
    '-grid_tables',
    '-gutenberg',
    '-hard_line_breaks',
    '-header_attributes',
    '-ignore_line_breaks',
    '-implicit_figures',
    '-implicit_header_references',
    '-inline_code_attributes',
    '-inline_notes',
    '+intraword_underscores',
    '-latex_macros',
    '-line_blocks',
    '-link_attributes',
    '+lists_without_preceding_blankline',
    '-markdown_attribute',
    '-markdown_in_html_blocks',
    '-mmd_header_identifiers',
    '-mmd_link_attributes',
    '-mmd_title_block',
    '-multiline_tables',
    '-native_divs',
    '-native_spans',
    '-old_dashes',
    '-pandoc_title_block',
    '+pipe_tables',
    '-raw_attribute',
    '+raw_html',
    '-raw_tex',
    '-rebase_relative_paths',
    '-short_subsuperscripts',
    '-shortcut_reference_links',
    '-simple_tables',
    '+space_in_atx_header',
    '-spaced_reference_links',
    '+startnum',
    '+strikeout',
    '-subscript',
    '-superscript',
    '-table_captions',
    '-task_lists',
    '+tex_math_dollars',
    '-tex_math_double_backslash',
    '-tex_math_single_backslash',
    '-yaml_metadata_block'
]
pdoc_args = ['--from', 'markdown_strict'+''.join(extra), '--katex', '--no-highlight', '--columns=2147483647']
replaces = {r'\bm a': r'a', r'\bm b': r'b'}  # 针对 LaTeX 和 KaTeX 的差异进行替换

with open('error.png', 'rb') as f:
    error_img = f.read()


def get_video_url(v_type, v_id, v_add):
    v_type = v_type.upper() if v_type == 'bv' else v_type
    url = f'https://www.bilibili.com/video/{v_type}{v_id}{v_add}'
    return url


def get_video_t(v_add):
    res = re.search('t=.*&?', v_add)
    if res:
        res = float(res.group()[2:])
    else:
        res = 0.0
    return res


def format_num(num):
    num_str = str(num)
    if len(num_str) < 2:
        num_str = (2 - len(num_str)) * '0' + num_str
    return num_str


def convert_t(sec):
    sec = int(sec)
    return f'{format_num(sec//60)}:{format_num(sec%60)}'


def get_video_data(v_type, v_id, v_add):
    res = requests.get(f'http://apiv2.magecorn.com/bilicover/get?type={v_type}&id={v_id}')
    url = eval(res.text)['url']
    title = eval(res.text)['title']
    return {
        'title': title,
        'cover_img': BytesIO(requests.get(url).content),
        'url': get_video_url(v_type, v_id, v_add),
        't': convert_t(get_video_t(v_add))
    }


def get_cover_img(url):
    data = url[len('bilibili:'):].split('?')
    v_id = data[0]
    v_type = 'av' if v_id.isdecimal() else v_id[:2].lower()
    v_id = v_id if v_id.isdecimal() else v_id[2:]
    v_add = '?' + data[1] if len(data) > 1 else ''
    if v_type not in ['av', 'bv'] or not v_id.isalnum():
        raise ValueError('不合理的 av/bv 号')
    return get_video_data(v_type, v_id, v_add)


def get_latex_url(args):
    # 加载 LaTeX 图片
    txt, is_inline = args
    try:
        if is_inline == 'img':
            if txt.startswith('bilibili:'):
                return get_cover_img(txt), is_inline
            file_data = requests.get(txt).content
            return BytesIO(file_data), is_inline
        if txt in replaces:
            txt = replaces[txt]
        txt = urllib.parse.quote(txt.replace('\r\n', '').replace('\n', ''))
        txt = urllib.parse.quote(txt)
        url = 'https://latex.vimsky.com/test.image.latex.php?' + \
              'fmt=png&val={inline}%255Cdpi%257B150%257D%2520%255Cfootnotesize%2520{txt}&dl=0'\
            .format(inline='%255Cinline%2520' if is_inline else '', txt=txt)
        file_data = requests.get(url).content
        return BytesIO(file_data), is_inline
    except:
        return BytesIO(error_img), is_inline


def get_latex_url_list(txt_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        results = executor.map(get_latex_url, txt_list)
    return results


def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    md5_value = md5_hash.hexdigest()
    return md5_value[:14]


class Load:
    def __init__(self, lazy_load_latex=True, use_cache=False):
        self.html = ""
        self.blocks = None
        self.img_url = {}
        self.bilibili_video = {}
        self.in_line_LaTeX: dict = {}  # 内联公式缓存
        self.LaTeX: dict = {}  # 行间公式缓存
        self.now_load_LaTeX = []  # 公式
        self.lazy_load_latex = lazy_load_latex  # 是否懒加载
        self.use_cache = use_cache
        self.can_update = 0

    def set_markdown(self, mdfile_path):
        # 加载 md 文件并解析为 HTML
        with open(mdfile_path, "r", encoding='utf-8') as f:
            md_string = ''.join(list(f))
        self.set_markdown_from_string(md_string)

    def set_markdown_from_string(self, md_string, temp=''):
        # 从字符串加载 md 代码并解析为 HTML
        md_string = re.sub(r'_{3,}', '\n---\n', md_string)
        with open('Article/' + calculate_md5(temp) + '.md_html', 'r', encoding='utf-8') as f:
            self.html = f.read()
        '''output = pypandoc.convert_text(md_string,
                                       to='html5',
                                       format='md',
                                       extra_args=pdoc_args,
                                       )
        self.html = '<html><head></head><body>'+output+'</body></html>'
        '''
        self.blocks = None
        self.parse_markdown_file()

    def load_latex(self):
        while len(self.now_load_LaTeX):
            gs, inline = self.now_load_LaTeX[0]
            if gs.startswith('bilibili:') and inline == 'img':
                sf = get_latex_url((gs, inline))[0]
                sf['cover_img'] = pygame.image.load_extended(sf['cover_img'])
                self.bilibili_video[gs] = sf
            else:
                dd = get_latex_url((gs, inline))[0]
                try:
                    sf = pygame.image.load_extended(dd)
                except:
                    self.now_load_LaTeX.pop(0)
                    continue
                if inline == 'img':
                    self.img_url[gs] = sf
                else:
                    if inline:
                        self.in_line_LaTeX[gs] = sf
                        if self.use_cache:
                            pygame.image.save(sf, 'images/' + calculate_md5(gs) + '.png')
                    else:
                        self.LaTeX[gs] = sf
                        if self.use_cache:
                            pygame.image.save(sf, 'images/' + calculate_md5(gs) + '.png')
            self.now_load_LaTeX.pop(0)
            # time.sleep(0.5)
            self.can_update = 1

    def parse_markdown_file(self):
        time_s = time.time()

        # 解析 HTML 代码
        self.blocks = bs4.BeautifulSoup(self.html, 'lxml').body
        self.img_url = {}
        self.bilibili_video = {}
        self.now_load_LaTeX = []

        li_tags = self.blocks.find_all('li')
        span_tags = self.blocks.find_all(['span', 'img'])
        pre_tags = self.blocks.find_all('pre')

        # 把嵌套列表改成内联标签
        for li in li_tags:
            ol_tags = li.find_all('ol')
            ul_tags = li.find_all('ul')
            for ol in ol_tags:
                ol.name = 'ol_nest'
            for ul in ul_tags:
                ul.name = 'ul_nest'

        # 下载 LaTeX 图片 和 img
        images = os.listdir('images') if self.use_cache else None
        loading_img = pygame.font.SysFont('SimHei', 16).render('LaTeX加载中...', True, (125, )*3)
        for span in span_tags:
            if span.name == 'span':
                # print(span)
                if span['class'] == ['math', 'inline']:
                    gs = str(span.contents[0])
                    if self.use_cache and calculate_md5(gs) + '.png' in images:
                        self.in_line_LaTeX[gs] = pygame.image.load('images/' + calculate_md5(gs) + '.png')
                        continue
                    if (gs, True) not in self.now_load_LaTeX and gs not in self.in_line_LaTeX:
                        self.now_load_LaTeX.append((gs, True))
                        self.in_line_LaTeX[gs] = loading_img
                else:
                    gs = str(span.contents[0])
                    if self.use_cache and calculate_md5(gs) + '_.png' in images:
                        self.LaTeX[gs] = pygame.image.load('images/' + calculate_md5(gs) + '_.png')
                        continue
                    if (gs, False) not in self.now_load_LaTeX and gs not in self.LaTeX:
                        self.now_load_LaTeX.append((gs, False))
                        self.LaTeX[gs] = loading_img
            else:
                src = span['src']
                if src.startswith('bilibili:'):
                    self.bilibili_video[src] = None
                    self.now_load_LaTeX.append((src, 'img'))
                    continue
                self.img_url[src] = pygame.image.load('error.png')
                self.now_load_LaTeX.append((src, 'img'))

        if not self.lazy_load_latex:
            res = get_latex_url_list(self.now_load_LaTeX)  # 下载
            for i, sf in enumerate(res):  # 存入缓存
                sf = sf[0]
                gs = self.now_load_LaTeX[i][0]
                if self.now_load_LaTeX[i][1] == 'img':
                    if gs.startswith('bilibili:'):
                        sf['cover_img'] = pygame.image.load_extended(sf['cover_img'])
                        self.bilibili_video[gs] = sf
                        continue
                    try:
                        self.img_url[gs] = pygame.image.load_extended(sf)
                    except:
                        print(f'{gs}的图片格式不支持')
                    continue
                if self.now_load_LaTeX[i][1]:
                    self.in_line_LaTeX[gs] = pygame.image.load_extended(sf)
                    if self.use_cache:
                        pygame.image.save(self.in_line_LaTeX[gs], 'images/' + calculate_md5(gs) + '.png')
                else:
                    self.LaTeX[gs] = pygame.image.load_extended(sf)
                    if self.use_cache:
                        pygame.image.save(self.LaTeX[gs], 'images/' + calculate_md5(gs) + '_.png')
        # 代码高亮
        for pre in pre_tags:  # 遍历所有的多行代码块
            lang = pre.get('class')  # 获取语言名
            if lang is not None:  # 有语言标注
                lang = ' '.join(lang)  # 语言名里有空格时会被 bs4 解析成列表，现在把语言名还原为字符串
            else:  # 无语言标注，不高亮
                pre.find('code').string += '\n'  # 给代码末尾追加换行
                continue
            code = CodeHilite(src=pre.find('code').string, lang=lang)  # 代码高亮（速度超级慢）
            html = bs4.BeautifulSoup(code.hilite(), 'lxml')  # 重新解析高亮后的代码
            pre.find('code').replace_with(html.find('code'))  # 替换未高亮的代码

        # print(self.blocks)
        print("markdown解析完成，用时{}s".format(time.time()-time_s))
        if self.lazy_load_latex:
            tt = thr.Thread(target=self.load_latex, args=(), name="T1")
            tt.start()


def load(file_name):
    data = Load(lazy_load_latex=True)
    data.set_markdown(file_name)
    return data


def load_string(string, temp=''):
    data = Load(lazy_load_latex=True)
    data.set_markdown_from_string(string, temp)
    return data
