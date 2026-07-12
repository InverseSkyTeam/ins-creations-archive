import os

def explorer(to='down'):
    if to == 'down':
        os.system('taskkill /f /im explorer.exe')
    else:
        print(1)
        os.system('cd C:/Windows && explorer')
        print(3)

# explorer('down')
# explorer('up')