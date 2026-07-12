print('小轩每日一水\n50行代码做伪语言框架\n语言名称：INSjhx\n开发者：无聊的逆天小轩\n用法:\nin "文本"\nin 数字\nin 变量 输入功能\nout "文本"\nout 数字\nout 变量 输出功能\nvar 变量名 = 要赋的值(字符串请加引号)\nvar 变量名 = in "内容"/数字/变量 相当于python里变量名=input(内容)\n上面变量赋值\n50行代码这些功能可以不\n\n\n编写区域-----')

class INSjhx:
    def __init__(self):
        self.command = ''
        self.keyword = ['in','out','var']
    def changecmd(self,command):
        self.command = command
    def run(self,command='settrue'):
        if command == 'settrue' and self.command['cmd'] in self.keyword:
            return eval('self.cmd'+self.command['cmd']+'()')
        elif command != 'settrue' and command['cmd'] in self.keyword:
            return eval('self.cmd'+command['cmd']+'(command=command)')
    def cmdin(self,command='settrue'):
        if command == 'settrue':
            return input(eval(self.command['content']))
        return input(eval(command['content']))
    def cmdout(self):
        print(eval(self.command['content']))
    def cmdvar(self):
        cmd = self.command['content'].split('=')
        cmd = [cmd[0],'='.join(cmd[1:])]
        is_double = 0
        for i in self.keyword:
            if i in cmd[1]:
                is_double = 1
        if is_double:
            if ' ' in cmd[1]:
                command = cmd[1].split()
                command = {'cmd':command[0],'content':' '.join(command[1:])}
                if command['cmd'] == 'no-space':
                    command['cmd'] = 'input-no-space'
            else:
                command = {'cmd':'no-space','content':text}
            cmd[1] = '"'+self.run(command=command)+'"'
        exec('global '+cmd[0]+'\n'+cmd[0]+'='+cmd[1])

insjhx = INSjhx()

while True:
    text = input('ins:>')
    if text.replace(' ','').replace('\t','').replace('\r','').replace('\n','') == '':
        continue
    if ' ' in text:
        command = text.split()
        command = {'cmd':command[0],'content':' '.join(command[1:])}
        if command['cmd'] == 'no-space':
            command['cmd'] = 'input-no-space'
    else:
        command = {'cmd':'no-space','content':text}
    insjhx.changecmd(command)
    insjhx.run()