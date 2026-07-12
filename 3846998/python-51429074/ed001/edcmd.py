class EdCmd:
    def __init__(self, head: str, body: str | None):
        self.head, self.body = head, body

    def run(self, cmdmap: dict):
        if self.body is not None:
            return cmdmap[self.head](self.body)
        else:
            return cmdmap[self.head](self.body)


def read_cmd(cmd: str) -> EdCmd | None:
    cmd = cmd.lstrip().rstrip()
    if cmd == '':
        return None
    s = cmd.split(' ', 1)
    if len(s) == 2:
        return EdCmd(s[0], s[1])
    else:
        return EdCmd(s[0], None)
