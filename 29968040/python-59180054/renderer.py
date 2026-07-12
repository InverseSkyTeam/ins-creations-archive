from typing import List


class Parser:
    def __init__(self, text: List[str]):
        self.text = text
        self.unk_begin = 0  # 还未被高亮的行 [0, unk_begin)
        self.changes = [False] * len(self.text)  # 每行是否有修改
        self.status = []  # 每行的尾状态，多用于多行字符串的高亮

    def change(self, index: int):
        self.unk_begin = min(self.unk_begin, index)
        self.changes[index] = True

    # [begin, end] 都是闭区间
    def add(self, begin: int, end: int):
        assert begin <= len(self.status)
        self.unk_begin = min(self.unk_begin, begin)
        self.changes = (
            self.changes[:begin] + \
            [True] * (end + 1 - begin) + \
            self.changes[begin:]
        )

    # [begin, end] 都是闭区间
    def remove(self, begin: int, end: int):
        assert end < len(self.status)
        self.unk_begin = min(self.unk_begin, begin + 1)
        del self.changes[begin : end + 1]

    def parse(self, target: int):  # 解析指定行的代码
        pass

    def get(self, y: int, x: int):
        pass
