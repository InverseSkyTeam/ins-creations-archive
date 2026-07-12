import re
import pypandoc
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
import sys


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


def get_latex_url(args):
    # 加载 LaTeX 图片
    txt, is_inline = args
    txt = urllib.parse.quote(txt.replace('\r\n', '').replace('\n', ''))
    txt = urllib.parse.quote(txt)
    url = 'https://latex.vimsky.com/test.image.latex.php?' + \
          'fmt=png&val={inline}%255Cdpi%257B150%257D%2520%255Cfootnotesize%2520{txt}&dl=0'\
        .format(inline='%255Cinline%2520' if is_inline else '', txt=txt)
    file_data = requests.get(url).content
    return BytesIO(file_data)


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
    def __init__(self):
        self.html = ""
        self.blocks = None
        self.img_url = {}
        self.in_line_LaTeX: dict = {}  # 内联公式缓存
        self.LaTeX: dict = {}  # 行间公式缓存
        self.in_line_LaTeX_data = {}
        self.LaTeX_data = {}

    def set_markdown(self, mdfile_path):
        # 加载 md 文件并解析为 HTML
        with open(mdfile_path, "r", encoding='utf-8') as f:
            md_string = ''.join(list(f))
        self.set_markdown_from_string(md_string)

    def set_markdown_from_string(self, md_string):
        # 从字符串加载 md 代码并解析为 HTML
        md_string = re.sub(r'_{3,}', '\n---\n', md_string)
        try:
            output = pypandoc.convert_text(md_string,
                                           to='html5',
                                           format='md',
                                           extra_args=pdoc_args,
                                           )
        except:
            print('请安装pypandoc_binary库再运行')
            sys.exit()
        self.html = '<html><head></head><body>'+output+'</body></html>'
        self.blocks = None
        self.parse_markdown_file()

    def parse_markdown_file(self):
        time_s = time.time()

        # 解析 HTML 代码
        self.blocks = bs4.BeautifulSoup(self.html, 'lxml').body
        self.img_url = {}

        li_tags = self.blocks.find_all('li')
        span_tags = self.blocks.find_all('span')
        pre_tags = self.blocks.find_all('pre')
        inline = []  # 内联公式
        not_inline = []  # 行间公式

        # 把嵌套列表改成内联标签
        for li in li_tags:
            ol_tags = li.find_all('ol')
            ul_tags = li.find_all('ul')
            for ol in ol_tags:
                ol.name = 'ol_nest'
            for ul in ul_tags:
                ul.name = 'ul_nest'

        # 下载 LaTeX 图片
        images = os.listdir('images')
        for span in span_tags:
            if span['class'] == ['math', 'inline']:
                gs = str(span.contents[0])
                if calculate_md5(gs) + '.png' in images:
                    self.in_line_LaTeX[gs] = pygame.image.load('images/' + calculate_md5(gs) + '.png')
                    continue
                if (gs, True) not in inline and gs not in self.in_line_LaTeX:
                    inline.append((gs, True))
            else:
                gs = str(span.contents[0])
                if calculate_md5(gs) + '_.png' in images:
                    self.LaTeX[gs] = pygame.image.load('images/' + calculate_md5(gs) + '_.png')
                    continue
                if (gs, False) not in not_inline and gs not in self.LaTeX:
                    not_inline.append((gs, False))

        res = get_latex_url_list(inline)  # 下载
        res1 = get_latex_url_list(not_inline)

        for i, sf in enumerate(res):  # 存入缓存
            self.in_line_LaTeX[inline[i][0]] = pygame.image.load_extended(sf)
            pygame.image.save(self.in_line_LaTeX[inline[i][0]], 'images/' + calculate_md5(inline[i][0]) + '.png')
        for i, sf in enumerate(res1):
            self.LaTeX[not_inline[i][0]] = pygame.image.load_extended(sf)
            pygame.image.save(self.LaTeX[not_inline[i][0]], 'images/' + calculate_md5(not_inline[i][0]) + '_.png')

        # 代码高亮
        for pre in pre_tags:  # 遍历所有的多行代码块
            lang = pre.get('class')  # 获取语言名
            if lang is not None:  # 有语言标注
                lang = ' '.join(lang)  # 语言名里有空格时会被bs4解析成列表，现在把语言名还原为字符串
            else:  # 无语言标注，不高亮
                pre.find('code').string += '\n'  # 给代码末尾追加换行
                continue
            code = CodeHilite(src=pre.find('code').string, lang=lang)  # 代码高亮
            html = bs4.BeautifulSoup(code.hilite(), 'lxml')  # 重新解析高亮后的代码
            pre.find('code').replace_with(html.find('code'))  # 替换未高亮的代码

        # print(self.blocks)
        print("markdown解析完成，用时{}s".format(time.time()-time_s))


def load(file_name):
    data = Load()
    data.set_markdown(file_name)
    return data

