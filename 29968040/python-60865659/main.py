import re
from py_linebreaker import LineBreaker, String

# 这些测试用例有问题，可能不正确或适配不同，跳过它们
SKIP = {
    125, 127, 815, 1161, 1163, 1165, 1167, 1331, 2189, 2191, 2873, 2875, 3567,
    3739, 4081, 4083, 4425, 4427, 4473, 4475, 4597, 4599, 4645, 4647, 4943,
    5109, 5111, 5459, 6149, 6151, 6153, 6155, 6489, 6491, 6663, 6833, 6835,
    7005, 7007, 7177, 7179, 7477, 7486, 7491, 7576, 7577, 7578, 7579, 7580,
    7581, 7583, 7584, 7585, 7586, 7587, 7604, 7610, 7611, 7681
}

with open('LineBreakTest.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

wrong = 0

for i, line in enumerate(lines):
    row_number = i + 1
    line = line.strip()
    if not line or line.startswith('#'):
        continue

    # 分割测试数据和注释
    if '#' in line:
        cols, comment = line.split('#', 1)
    else:
        cols, comment = line, ''
    cols = cols.strip()

    # 解析Unicode代码点
    parts = re.split(r'\s*[×÷]\s*', cols)
    code_points = [int(p, 16) for p in parts[1:-1] if p]

    # 构建测试字符串
    test_str = String(''.join(chr(cp) for cp in code_points))

    # 执行断行操作
    breaker = LineBreaker(test_str)
    breaks = []
    last = 0
    while True:
        bk = breaker.nextBreak()
        if not bk:
            break
        breaks.append(test_str.data[last * 2: bk.position * 2].decode('utf-16be'))
        last = bk.position

    # 解析预期结果
    expected = []
    for segment in re.split(r'\s*÷\s*', cols)[:-1]:
        codes = re.split(r'\s*×\s*', segment.strip())
        codes = [c for c in codes if c]  # 过滤空字符串
        if not codes:
            expected.append('')
            continue
        expected.append(''.join(chr(int(c, 16)) for c in codes))

    # 跳过指定用例
    if row_number in SKIP:
        print(f'跳过第 {row_number} 行，因为测试样例可能有问题\n')
        continue

    # 验证结果
    if breaks == expected:
        print(f'第 {row_number} 行成功\n实际: {breaks}\n预期: {expected}\n注释: {comment.strip()}\n')
    else:
        print(f'第 {row_number} 行失败\n实际: {breaks}\n预期: {expected}\n注释: {comment.strip()}\n')
        wrong += 1

print(f"所有测试完成，有 {wrong} 次测试失败")