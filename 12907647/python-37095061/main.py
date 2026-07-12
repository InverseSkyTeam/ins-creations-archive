import loadnews
import sys
database = []
variabledb = []
codetype = 'insjhx'
codecmdline = ''
codepool = {}
el = '\n'
tab = '    '
spc = ' '
Version = 'V0.5+ build176 [insjhx] 逆天小轩 all rights reversed.'
VersionNews = loadnews.text

keywords = [
    'var',
    'vars',
    'space',
    'int',
    'str',
    'list',
    'in',
    'out',
    'ord',
    'chr',
    'cut',
    'db',
    'index',
    'calc',
    'calc-ex',
    'help',
    '$!do!$',
    '$!enddo!$',
    # '',
    # '',
    ]

class LineRunner(object):
    def __init__(self,command):
        self.command = command
        self.helptext = '该版本(0.5s)仅作为分支，不开放帮助，请点击改编查看'
        if self.command.replace(' ','').replace('\n','').replace('\t','') == '':
            self.commandlist = ['space',self.command]
        else:
            self.commandlist = command.split()
            if len(self.commandlist) < 2:
                self.commandlist = ['space',self.commandlist[0]]
            else:
                self.commandlist = [self.commandlist[0],' '.join(self.commandlist[1:])]
    def run(self):
        global codetype,codepool,codecmdline
        if codetype in ['insjhx','default'] or ('$!' in self.command and '!$' in self.command):
            ans = ''
            insidecmd = self.commandlist[1].split()
            if len(insidecmd) > 1:
                insidecmd = [insidecmd[0],' '.join(insidecmd[1:])]
                if insidecmd[0] in keywords:
                    try:
                        eval(insidecmd[0]+' '+insidecmd[1])
                    except:
                        try:
                            insiderunner = LineRunner(insidecmd[0]+' '+insidecmd[1])
                            ansinside = str(insiderunner.run())
                            self.commandlist[1] = ansinside
                            print('doing inside okay:ret',ansinside)
                        except:
                            pass
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
                elif self.commandlist[0] == 'ord':
                    ans = self.cmd_ord(eval(self.commandlist[1]))
                elif self.commandlist[0] == 'chr':
                    ans = self.cmd_chr(eval(self.commandlist[1]))
                elif self.commandlist[0] == 'index':
                    cmd = self.commandlist[1].split()
                    cmd[0] = eval(cmd[0])
                    if ':' not in cmd[1]:
                        cmd[1] = int(cmd[1])
                    ans = self.cmd_index(cmd)
                elif self.commandlist[0] == 'cut':
                    ans = self.cmd_cut(eval(self.commandlist[1]))
                elif self.commandlist[0] == 'help':
                    if self.commandlist[1] == '/':
                        ans = self.cmd_help()
                elif self.commandlist[0] == 'db':
                    cmd = self.commandlist[1].split()
                    cmd = [cmd[0],' '.join(cmd[1:])]
                    ans = self.cmd_calldb(eval(cmd[1]),cmd[0])
                elif self.commandlist[0] == 'var':
                    cmd = self.commandlist[1].split('=')
                    cmd = [cmd[0],'='.join(cmd[1:])]
                    ans = self.cmd_var(cmd)
                elif self.commandlist[0] == 'vars':
                    ans = self.cmd_vars(self.commandlist[1])
                elif self.commandlist[0] == 'space':
                    ans = 'non ret text:['+self.commandlist[1]+']'
                elif self.commandlist[0] == 'cs':
                    print('\033[2J\033[100A\033[3J\033[100A'*16)
                    ans = 'cleaned screen.'
                elif self.commandlist[0] == 'calc':
                    ans = eval(self.commandlist[1])
                elif self.commandlist[0] == 'calc-ex':
                    ans = self.cmd_calcex(self.commandlist[1])
                elif self.commandlist[0] == '$!do!$':
                    ans = self.cmd_h_do(self.commandlist[1])
                elif self.commandlist[0] == '$!enddo!$':
                    ans = self.cmd_h_enddo()
                else:
                    ans = '[Error|OutWarn] undefined command.'
            except:
                ans = '[Error|OutError] except in outing.'
            return ans
        else:
            codecmdline += self.command + '\n'
        return 'read in.'
    def cmd_out(self,cmd):
        return cmd
    def cmd_in(self,cmd):
        return input(cmd)
    def cmd_int(self,cmd):
        return int(cmd)
    def cmd_str(self,cmd):
        return '"'+str(cmd)+'"'
    def cmd_list(self,cmd):
        return list(cmd)
    def cmd_ord(self,cmd):
        return '"'+ord(cmd)+'"'
    def cmd_chr(self,cmd):
        return chr(cmd)
    def cmd_cut(self,cmd):
        return cmd.split()
    def cmd_index(self,cmd):
        if type(cmd[1]) == str:
            return eval(str(cmd[0])+'['+cmd[1]+']')
        return cmd[0][cmd[1]]
    def cmd_calcex(self,cmd):
        cmd = cmd.replace('plus','+') \
                 .replace('minus','-') \
                 .replace('multi','*') \
                 .replace('divi','/') \
                 .replace('加','+') \
                 .replace('减','-') \
                 .replace('乘','*') \
                 .replace('除','/') \
                 .replace('big','>') \
                 .replace('sml','<') \
                 .replace('same','=') \
                 .replace('大于','>') \
                 .replace('小于','<') \
                 .replace('等于','=') \
                 .replace('mod','%') \
                 .replace('|','//') \
                 .replace('%','/100') \
                 .replace('[','(') \
                 .replace(']',')')
        return eval(cmd)
    def cmd_h_do(self,cmd):
        global codetype,codepool,codecmdline
        reply = '[Error|CodetypeError] unknow(bad) program lanuage.'
        if cmd in ['python','python3']:
            reply = 'set default format codetype:[python]'
        elif cmd == 'python2':
            reply = 'set format codetype:[python2];but I think use python3 is better'
        elif cmd in ['cpp','c++','cplusplus','c++20','c++17','c++14']:
            reply = 'set good format codetype:[c++],start your algorithm way!'
        elif cmd in ['c++11','c++98']:
            reply = 'set format codetype:[old-c++];you can use c++20'
        elif cmd == 'java':
            reply = 'set good format codetype:[java]'
        elif cmd == 'php':
            reply = 'set good format codetype:[php]'
        elif cmd == 'ruby':
            reply = 'set good format codetype:[ruby]'
        codecmdline = ''
        codetype = cmd
        return reply
    def cmd_h_enddo(self):
        global codetype,codepool,codecmdline
        if codetype in ['python','python3']:
            ff = 'cmd [vars] to sho all the vars,no out.'
            try:
                exec(codecmdline,globals())
            except Exception as e:
                ff += '\n'+e
            codepool[codecmdline] = ['python3',ff]
        else:
            pass
        reply = 'Executed.\nset default new codetype:[insjhx],welcome back home!'
        codetype = 'insjhx'
        return reply
    def cmd_var(self,cmd):
        try:
            exec('global '+cmd[0]+'\n'+cmd[0]+'='+cmd[1])
            reply = 'variable '+cmd[0]+' is success.'
            variabledb.append(cmd[0])
        except:
            try:
                linerunnerplus = LineRunner(cmd[1])
                answerplus = linerunnerplus.run()
                answerplus = str(answerplus)
                print('['+str(answerplus)+'] returned.\ndouble command run success.')
                try:
                    eval(answerplus)
                except:
                    answerplus = '"'+str(answerplus)+'"'
                exec('global '+cmd[0]+'\n'+cmd[0]+'='+answerplus)
                reply = 'variable '+cmd[0]+' is success.'
                variabledb.append(cmd[0])
            except:
                reply = '[Error|VariableError] bad command and out error in varing.'
        return reply
    def cmd_vars(self,cmd):
        if cmd == 'view':
            return variabledb
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
        else:
            reply = '[Error|DataBaseError] db command except.'

print('教程输入“help /”即可查看')
while 1:
    cmd = input('ins:>')
    linerunner = LineRunner(cmd)
    answer = linerunner.run()
    print(answer)