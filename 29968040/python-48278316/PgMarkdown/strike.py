# 这个是 markdown 的自定义扩展，用于 markdown 库解析删除线
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


class DelInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('s')
        el.text = m.group(1)
        return el, m.start(0), m.end(0)


class DelExtension(Extension):
    def extendMarkdown(self, md):
        DEL_PATTERN = r'~~(.*?)~~'  # like ~~del~~
        md.inlinePatterns.register(DelInlineProcessor(DEL_PATTERN, md), 's', 175)
