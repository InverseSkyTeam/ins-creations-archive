import random,time,sys,webbrowser as w
print('Hello!from jhxSystem DOS 0.1 tip-local-command input line<<(C:)fs NTFS')
print('jhxSystem DOS [Version 0.1 beta-test]')
print('upload.')
print('(c)INS-jhx Copyright.2021,2022')
print('\n\n')
print('type "help" to know how to drive it. ')

insert_lines = {
    'cls':'clean the all of screen',
    'enter':'do enter',
    'exit':'exit the system',
    'help':'read help texts about the system run',
    'init_GUIV':'init GUI Version to drive this system',
    'pip_init_on':'turn on installed inited GUI and use',
    'quit':'same as "exit"',
    'show_pips':'show the GUI systems if you can use',
}

def help_index(index='main',inserts=insert_lines):
    if index == 'main':
        for i in inserts:
            print('|'+i+' '*(15-len(i))+'|'+inserts[i])

while True:
    print('{C:}insert line>>',end='')
    localcommand = input()
    if localcommand in insert_lines or localcommand == '':
        if 'cls' == localcommand:
            print('\033[100A\033[2J\033[100A\033[3J'*2)
        if 'help' == localcommand:
            help_index()
        if 'show_pips' == localcommand:
            print('''pips(0)''')
        if 'exit' == localcommand or 'quit' == localcommand:
            sys.exit()
        if 'init_GUIV' == localcommand or 'pip_init_on' == localcommand:
            print('There\'re not any jhx-INS-DreamLightComputerSytem GUIVs.')
    else:
        print('How are you?If you don\'t know how to drive the system,you can type "help".')