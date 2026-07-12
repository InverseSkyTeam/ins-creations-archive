from __future__ import annotations

import re

from .my_trim import WhiteSpace


# Luogu Dev: 始终识别为有效的分隔符
def isValidDelim(state, pos):
    return {
        'can_open': True,
        'can_close': True
    }


def math_inline(state, silent):
    if state.src[state.pos] != "$":
        return False

    res = isValidDelim(state, state.pos)
    if not res['can_open']:
        if not silent:
            state.pending += "$"
        state.pos += 1
        return True

    # 首先检查并跳过所有正确转义的分隔符
    # 这个循环假设第一个前导反引号不能是 state.src 中的第一个字符
    # 这是已知的，因为我们已经找到了一个开头的分隔符。
    start = state.pos + 1
    match = start
    while state.src.find("$", match) != -1:
        match = state.src.find("$", match)
        # 找到潜在的 $ 符号，检查转义，
        # pos 会指向完成时第一个未转义的位置
        pos = match - 1
        while state.src[pos] == "\\":
            pos -= 1

        # 转义次数为偶数，找到潜在的闭合分隔符
        if (match - pos) % 2 == 1:
            break
        match += 1

    # No closing delimter found.  Consume $ and continue.
    if match == -1:
        if not silent:
            state.pending += "$"
        state.pos = start
        return True

    # Check if we have empty content, ie: $$.  Do not parse.
    if match - start == 0:
        if not silent:
            state.pending += "$$"
        state.pos = start + 1
        return True

    # Check for valid closing delimiter
    res = isValidDelim(state, match)
    if not res['can_close']:
        if not silent:
            state.pending += "$"
        state.pos = start
        return True

    if not silent:
        token = state.push('math_inline', 'math', 0)
        token.markup = "$"
        token.content = state.src[start:match]

    state.pos = match + 1
    return True


def math_block(state, start, end, silent):
    lastLine = None
    found = False
    pos = state.bMarks[start] + state.tShift[start]
    max = state.eMarks[start]

    if pos + 2 > max:
        return False
    if state.src[pos:pos+2] != '$$':
        return False

    pos += 2
    firstLine = state.src[pos:max]

    if silent:
        return True
    if firstLine.strip(WhiteSpace)[-2:] == '$$':
        # Single line expression
        firstLine = firstLine.strip(WhiteSpace)[0:-2]
        found = True

    next = start
    while not found:
        next += 1

        if next >= end:
            break

        pos = state.bMarks[next]+state.tShift[next]
        max = state.eMarks[next]

        if pos < max and state.tShift[next] < state.blkIndent:
            # non-empty line with negative indent should stop the list:
            break

        if state.src[pos:max].strip(WhiteSpace)[-2:] == '$$':
            lastPos = state.src[0:max].rfind('$$')
            lastLine = state.src[pos:lastPos]
            found = True

    if next >= end:
        return False
    
    _first = firstLine + '\n' if (firstLine and firstLine.strip(WhiteSpace)) else ''
    _txt = state.getLines(start + 1, next, state.tShift[start], True)
    _last = lastLine if (lastLine and lastLine.strip(WhiteSpace)) else ''
    state.line = next + 1

    token = state.push('math_block', 'math', 0)
    token.block = True
    token.content = _first + _txt + _last
    token.map = [start, state.line]
    token.markup = '$$'
    return True


def math_plugin(md, options=None):
    options = options or {}
    
    def escapeHtml(html):
        tagsToReplace = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;'
        }
        return re.sub('[&<>]', lambda match: tagsToReplace[match.group(0)], html)

    # set KaTeX as the renderer for markdown-it-simplemath
    def katexInline(latex):
        options['displayMode'] = False
        return escapeHtml(latex)

    def inlineRenderer(self, tokens, idx, options, env):
        html = katexInline(tokens[idx].content)

        return '<span class="math inline">' + html + '</span>'

    def katexBlock(latex):
        options['displayMode'] = True
        return escapeHtml(latex)

    def blockRenderer(self, tokens, idx, options, env):
        html = katexBlock(tokens[idx].content)
        return '<p><span class="math">' + html + '</span></p>\n'

    md.inline.ruler.after('escape', 'math_inline', math_inline)
    md.block.ruler.after('blockquote', 'math_block', math_block, {
        'alt': ['paragraph', 'reference', 'blockquote', 'list']
    })
    md.add_render_rule('math_inline', inlineRenderer)
    md.add_render_rule('math_block', blockRenderer)
