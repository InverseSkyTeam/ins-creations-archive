import os
import sys
def get_py_path():
    return sys.executable
def install_library():
    try:
        import icu
    except ImportError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        try:
            subprocess.check_call([get_py_path(), '-m', 'pip', 'install', "PyICU-2.8.1-cp37-cp37m-win32.whl"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)
install_library()


import text_break_iterator as text_break
print('kNormal:', text_break.test('標（準）萬ab國.碼', 'kNormal'))
print('kBreakAll:', text_break.test('標（準）萬ab國.碼', 'kBreakAll'))