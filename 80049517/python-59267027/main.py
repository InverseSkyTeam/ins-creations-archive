print("Linux Python 下有效的 getch/kbhit")
print("非常感谢 DeepSeek 提供了代码（")

import sys
import os
import termios
import select
import atexit

class _Getch:
    def __init__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        
        # 设置新的终端属性：非规范模式、关闭回显
        new = termios.tcgetattr(self.fd)
        new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
        new[6][termios.VMIN] = 0  # 读取最小字符数
        new[6][termios.VTIME] = 0 # 读取超时（十分之一秒）
        
        # 应用新设置
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, new)
        
        # 注册退出恢复函数
        atexit.register(self._restore)

    def _restore(self):
        """恢复原有终端设置"""
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_settings)

    def kbhit(self):
        """检测是否有键盘输入（非阻塞）"""
        rlist, _, _ = select.select([self.fd], [], [], 0)
        return len(rlist) > 0

    def getch(self):
        """获取单个字符（阻塞模式）"""
        # 等待输入可用
        select.select([self.fd], [], [])
        return os.read(self.fd, 1).decode('utf-8', 'ignore')

# 单例模式实例
_getch = _Getch()

def kbhit():
    return _getch.kbhit()

def getch():
    return _getch.getch()

# 示例用法
if __name__ == '__main__':
    print("Press any key (ESC to exit):")
    while True:
        if kbhit():
            c = getch()
            print(f"Pressed: {c} (ASCII: {ord(c)})")
            if c == '\x1b':  # ESC键
                break
