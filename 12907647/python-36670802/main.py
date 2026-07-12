import sys
database = []

class LineRunner(object):
    def __init__(self,command):
        self.command = command
        self.helptext = '''[insjhxpy help text]
Copyright INS(c) -jhx /py 2022years
%python->insjhx%

"ins:"means you should input command

out -> print sth
in -> input sth
int -> int sth
str -> str sth
space -> same as "#" in python
cut "a b cd e fg" -> ["a","b","cd","e","fg"]
list -> list sth
help / -> help text
db add sth -> append sth to global db
db del sth -> delete sth from global db
db index sth -> index sth from global db
db find sth -> find sth from global db

example:
ins:out "hello"
hello
ins:out 1+2+3==1*2*2
True
ins:in "input sth>>"
input sth>>666
666
ins:space 1

ins:int "666"
666
ins:help /
...(this help)
ins:db add 666
add 666
ins:db add "hello"
add hello
ins:index 666
0
ins:find 1
hello
ins:del 666
del 666
ins:find 1
1 is a bad index
ins:find 0
hello

thank you for view the helptext,you can type "help /" to see it again
now you can code.
'''
        if self.command.replace(' ','').replace('\n','').replace('\t','') == '':
            self.commandlist = ['space',self.command]
        else:
            self.commandlist = command.split()
            if len(self.commandlist) < 2:
                self.commandlist = ['space',self.commandlist[0]]
            else:
                self.commandlist = [self.commandlist[0],' '.join(self.commandlist[1:])]
    def run(self):
        ans = ''
        try:
            if self.commandlist[0] == 'out':
                ans = self.cmd_out(eval(self.commandlist[1]))
            elif self.commandlist[0] == 'in':
                ans = self.cmd_in(eval(self.commandlist[1]))
            elif self.commandlist[0] == 'int':
                ans = self.cmd_int(eval(self.commandlist[1]))
            elif self.commandlist[0] == 'str':
                ans = self.cmd_str(eval(self.commandlist[1]))
            elif self.commandlist[0] == 'list':
                ans = self.cmd_list(eval(self.commandlist[1]))
            elif self.commandlist[0] == 'cut':
                ans = self.cmd_cut(eval(self.commandlist[1]))
            elif self.commandlist[0] == 'help':
                ans = self.cmd_help()
            elif self.commandlist[0] == 'db':
                cmd = self.commandlist[1].split()
                cmd = [cmd[0],' '.join(cmd[1:])]
                ans = self.cmd_calldb(eval(cmd[1]),cmd[0])
        except:
            ans = 'out except'
        return ans
    def cmd_out(self,cmd):
        return cmd
    def cmd_in(self,cmd):
        return input(cmd)
    def cmd_int(self,cmd):
        return int(cmd)
    def cmd_str(self,cmd):
        return str(cmd)
    def cmd_list(self,cmd):
        return list(cmd)
    def cmd_cut(self,cmd):
        return cmd.split()
    def cmd_help(self):
        return self.helptext
    def cmd_calldb(self,cmd,do):
        if do == 'add':
            database.append(cmd)
            return 'add '+str(cmd)
        elif do == 'del':
            database.remove(cmd)
            return 'del '+str(cmd)
        elif do == 'index':
            try:
                cmd = str(cmd)+' index '+str(database.index(cmd))
            except:
                cmd = str(cmd)+' not in database'
            return cmd
        elif do == 'find':
            try:
                cmd = database[cmd]
            except:
                cmd = str(cmd)+' is a bad index'
            return cmd


print('教程输入“help /”即可查看')
while 1:
    cmd = input('ins:')
    linerunner = LineRunner(cmd)
    answer = linerunner.run()
    print(answer)