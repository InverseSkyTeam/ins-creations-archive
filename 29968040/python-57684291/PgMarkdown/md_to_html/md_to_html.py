from markdown_it import MarkdownIt
from .math_plugin import math_plugin

md = MarkdownIt("js-default").use(math_plugin)


def md_to_html(md_string):
    output = md.render(md_string)
    # print(output)
    return '<html><head></head><body>'+output+'</body></html>'
