import loadnews
import sys
database = []
variabledb = []
codetype = 'insjhx'
codecmdline = ''
codepool = {}
endl = '\n'
tab = '    '
spc = ' '
Version = 'V0.6 build 400 [insjhx] 逆天小轩 all rights reversed.'
VersionNews = loadnews.text
runnerstatu = 'good'

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
    'cfg',
    'if',
    'elif',
    'else',
    'for',
    'while',
    '$!do!$',
    '$!enddo!$',
    '$!exit!$',
    # '',
    ]

CONSTS = [
    'el',
    'tab',
    'spc',
    'Version',
    'VersionNews',
    ]

configs = {
    'mode':'normal',   # normal strict(严格模式) simple(老年人模式/doge)
    # '':'',
    # '':'',
    # '':'',
    # '':'',
    # '':'',
    # '':'',
    # '':'',
    # '':'',
    # '':'',
    # '':'',
    # '':'',
}

indent_pool = []
indentkeyword = ''

class ParseMethod(object):
    def __init__(self):
        self.name = 'parser'
    def __str__(self):
        return self.name
    __repr__ = __str__
    
    @classmethod
    def findmost(cls,text) -> tuple:
        insidelist = []
        indexlist = []
        insidetext = ''
        inside = 0
        textinside = 0
        textinside2 = 0
        index = -1
        for i in text:
            index += 1
            if i == '(' and textinside == 0 and textinside2 == 0:
                if inside == 0:
                    insidetext = ''
                    indexlist.append([index])
                else:
                    insidetext += '('
                inside += 1
            elif i == ')' and textinside == 0 and textinside2 == 0:
                inside -= 1
                if inside == 0:
                    insidelist.append(insidetext)
                    indexlist[-1].append(index+1)
                else:
                    insidetext += ')'
            elif i == '"':
                insidetext += '"'
                if textinside:
                    textinside = 0
                else:
                    textinside = 1
            elif i == "'":
                insidetext += "'"
                if textinside2:
                    textinside2 = 0
                else:
                    textinside2 = 1
            else:
                insidetext += i
        return (insidelist,indexlist)
    
    @classmethod
    def has_inside(cls,text) -> (tuple,str,bool):
        count = [0,0]
        for i in text:
            if i == '(':
                count[0] += 1
            elif i == ')':
                count[1] += 1
        if count[0] == count[1]:
            if count[0] == 0:
                return 'pass'
            return cls.findmost(text)
        x = cls.findmost(text)
        if x[0]:
            return x
        return False
    
    @classmethod
    def must_indent(cls) -> bool:
        global indentkeyword
        if indentkeyword:
            return True
        return False

parser = ParseMethod()

class CodesRunner(object):
    ...

class LineRunner(CodesRunner):
    def __init__(self,command):
        self.command = command
        self.helptext = '0.6的帮助懒得写，自己点击改编查看；out VersionNews输出更新日志'
        if self.command.replace(' ','').replace('\n','').replace('\t','') == '':
            self.commandlist = ['space',self.command]
        else:
            if parser.must_indent():
                count = 0
                while command[:4] == '    ':
                    count += 1
                    command = command[4:]
                self.commandlist = command.split()
                if count:
                    self.commandlist[0] = '    '*count + self.commandlist[0]
            else:
                self.commandlist = command.split()
            if len(self.commandlist) < 2:
                self.commandlist = ['space',self.commandlist[0]]
            else:
                self.commandlist = [self.commandlist[0],' '.join(self.commandlist[1:])]
    def run(self) -> str:   # 运行单行 # 我是水印小轩
        global codetype,codepool,codecmdline,indent_pool,indentkeyword
        if codetype in ['insjhx','default'] or ('$!' in self.command and '!$' in self.command):
            ans = ''  # 初始化回应
            # 缩进语句判断，if while for def class等
            sp_assign = self.commandlist[1].split('=')
            is_assign = len(sp_assign) == 2 and not sp_assign[0][0].isdigit() and configs['mode'] != 'strict'
            if parser.must_indent() and (self.commandlist[0] != 'space' or is_assign):
                if self.command[:4] == '    ':
                    if self.commandlist[0][:4] == '    ':
                        if len(indent_pool[-1]) < 3:
                            indent_pool[-1].append(self.commandlist[0][4:]+' '+self.commandlist[1])
                        else:
                            indent_pool[-1][2] += '\n' + self.commandlist[0][4:]+' '+self.commandlist[1]
                    else:
                        if len(indent_pool[-1]) < 3:
                            indent_pool[-1].append(self.commandlist[1][4:])
                        else:
                            indent_pool[-1][2] += '\n' + self.commandlist[1][4:]
                    return '----added to if.'
                else:
                    if indentkeyword == 'if':
                        if self.commandlist[0] not in ['elif','else']:
                            indentkeyword = ''
                            if len(indent_pool[-1]) == 2:
                                del indent_pool[-1]
                                return '[Error|IndentError] the inside indent is bad.'
                            
                            
                            
                            
                            # run if
                            try:
                                if eval(indent_pool[-1][1]):
                                    self.blockrunner = BlockRunner(indent_pool[-1][2])
                                    self.blockrunner.quickruncode()
                                print('if-block ok.')
                            except:
                                print('[Error|IfError] the code in if-block is bad.')
                            
                            
                            
                            
                            
                            
                            
                            # ...-more-...
                            
                            
                            del indent_pool[-1]
            
            getinside = parser.has_inside(self.commandlist[1])
            if not getinside:
                ans = '[Error|LevelError|ParenthesesError] the parentheses level is bad:not symmetry.'
                return ans
            if type(getinside) == tuple:     # 括号优先计算
                commandlisttextsplit = list(self.commandlist[1])
                for i in getinside[0]:
                    insidecmd = i.split()
                    if len(insidecmd) > 1:
                        insidecmd = [insidecmd[0],' '.join(insidecmd[1:])]
                        if insidecmd[0] in keywords:
                            try:
                                ansinside = eval(insidecmd[0]+' '+insidecmd[1])
                                fcase = getinside[1][getinside[0].index(i)]
                                commandlisttextsplit[fcase[0]:fcase[1]] = [ansinside]
                                print('--level inside ret:',ansinside)
                            except:
                                try:
                                    insiderunner = LineRunner(insidecmd[0]+' '+insidecmd[1])
                                    ansinside = str(insiderunner.run())
                                    fcase = getinside[1][getinside[0].index(i)]
                                    commandlisttextsplit[fcase[0]:fcase[1]] = [ansinside]
                                    print('--level inside ret:',ansinside)
                                except:
                                    ans = '[Error|RuntimeError|InsidelevelrunError] inside ans bad.'
                                    return ans
                self.commandlist[1] = ''.join(commandlisttextsplit)
            
            if configs['mode'] != 'strict':    # int str int多重嵌套
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
                                print('--inside ret:',ansinside)
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
                    ans = self.cmd_index(cmd)
                elif self.commandlist[0] == 'find':
                    cmd = self.commandlist[1].split()
                    ans = self.cmd_find(cmd)
                elif self.commandlist[0] == 'change':
                    cmd = self.commandlist[1].split()
                    ans = self.cmd_change(cmd)
                elif self.commandlist[0] == 'add':
                    cmd = self.commandlist[1].split()
                    ans = self.cmd_add(cmd)
                elif self.commandlist[0] == 'del':
                    ans = self.cmd_del(self.commandlist[1])
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
                elif self.commandlist[0] == 'cfg':
                    cmd = self.commandlist[1].split()
                    cmd = [cmd[0],'='.join(cmd[1:])]
                    ans = self.cmd_cfg(cmd)
                elif self.commandlist[0] == 'space':
                    cmd = self.commandlist[1].split('=')
                    if len(cmd) == 2 and configs['mode'] != 'strict':
                        cmd = [cmd[0],'='.join(cmd[1:])]
                        ans = self.cmd_var(cmd)
                    else:
                        ans = 'non ret text:['+self.commandlist[1]+']'
                elif self.commandlist[0] == 'cs':
                    print('\033[2J\033[100A\033[3J\033[100A'*16)
                    ans = 'cleaned screen.'
                elif self.commandlist[0] == 'calc':
                    ans = eval(self.commandlist[1])
                elif self.commandlist[0] == 'calc-ex':
                    ans = self.cmd_calcex(self.commandlist[1])
                elif self.commandlist[0] == 'if':
                    ans = self.cmd_i_if(self.commandlist[1])
                elif self.commandlist[0] == '$!do!$':
                    ans = self.cmd_h_do(self.commandlist[1])
                elif self.commandlist[0] == '$!enddo!$':
                    ans = self.cmd_h_enddo()
                elif self.commandlist[0] == '$!exit!$':
                    ans = self.cmd_h_exit(eval(self.commandlist[1]))
                else:
                    if configs['mode'] != 'strict':
                        self.commandlist = ['space',self.commandlist[0]+self.commandlist[1]]
                        cmd = self.commandlist[1].split('=')
                        if len(cmd) == 2:
                            cmd = [cmd[0],'='.join(cmd[1:])]
                            ans = self.cmd_var(cmd)
                        else:
                            if self.commandlist[1][0:5] == 'space':
                                self.commandlist[1] = self.commandlist[1][5:]
                            ans = 'non ret text:['+self.commandlist[1]+']'
                    else:
                        ans = '[Error|OutWarn] undefined command.'
            except SystemExit as e:
                ans = '[Log|Exitrunner] Exiting...\n[-msg]statu '+str(e)
            except NameError as e:
                ans = '[Error|NameError] name(var/fun/cls/mdl/cfg/err/log) not defined.\n[-msg]statu '+str(e)
            except SyntaxError as e:
                ans = '[Error|SyntaxError] invalid syntax.\n[-msg]statu '+str(e)
            except RuntimeError as e:
                ans = '[Error|RuntimeError] bad error when exec the code.\n[-msg]statu '+str(e)
            except Exception as e:
                ans = '[Error|OutError] except in outing.\n[-msg]'+str(e)
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
        return eval(str(cmd[0])+'['+cmd[1]+']')
    def cmd_find(self,cmd):
        return eval(str(cmd[0])+'.index('+cmd[1]+')')
    def cmd_change(self,cmd):
        if type(eval(cmd[0])) == str:
            return eval(str(cmd[0])+'.replace('+cmd[1]+','+cmd[2]+')')
        try:
            exec('global '+str(cmd[0])+'\n'+str(cmd[0])+'['+cmd[1]+'] = '+cmd[2])
            return 'changed success.'
        except:
            return '[Error|VariableError] cannot change a const.'
    def cmd_add(self,cmd):
        if type(eval(cmd[0])) == list:
            exec('global '+str(cmd[0])+'\n'+str(cmd[0])+'.append('+cmd[1]+')')
        else:
            exec('global '+str(cmd[0])+'\n'+str(cmd[0])+'['+cmd[1]+'] = '+cmd[2])
        return 'added success.'
    def cmd_del(self,cmd):
        exec('global '+str(cmd)+'\ndel '+str(cmd))
        return 'deleted success.'
    
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
    
    def cmd_cfg(self,cmd):
        if cmd[1]:
            configs[cmd[0]] = eval(cmd[1])
            return 'config:'+cmd[0]+' changed->'+cmd[1]
        try:
            return configs[cmd[0]]
        except:
            return '[Error|ConfigError|UnknowConfigError] read in an unknow cfg.'
    
    def cmd_var(self,cmd):
        try:
            exec('global '+cmd[0]+'\n'+cmd[0]+'='+cmd[1])
            reply = 'variable '+cmd[0].replace(' ','')+' is success.'
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
                reply = 'variable '+cmd[0].replace(' ','')+' is success.'
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
    
    def cmd_i_if(self,cmd):
        global indent_pool,indentkeyword
        indent_pool.append(['if',cmd])
        indentkeyword = 'if'
        return '--is in if'
    
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
            ff = 'cmd [vars] to show all the vars,no out.'
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
    def cmd_h_exit(self,quitcode):
        global runnerstatu
        if type(quitcode) in [tuple,list]:
            if quitcode:
                quitcode = quitcode[0]
            else:
                return '[Error|ExitError] exit list/tuple is empty.'
        if type(quitcode) not in [str,int,tuple,list]:
            return '[Error|ExitError] exit value is bad.'
        if int(quitcode) == 0:
            print('exit by good-quitcode 0.')
            runnerstatu = 'exit_0'
            sys.exit(0)
        else:
            print('exit by bad-quitcode '+str(quitcode)+'.')
            runnerstatu = 'exit_1'
            sys.exit(1)

class BlockRunner(CodesRunner):
    def __init__(self,codes):
        self.codelist = codes.replace('\t','    ').split('\n')
        self.lrun = CodesRunner()
        self.anslist = []
    def runcode(self):
        for self.codeline in self.codelist:
            self.lrun = LineRunner(self.codeline)
            self.anslist.append(str(self.lrun.run()))
    def quickruncode(self):
        for self.codeline in self.codelist:
            self.lrun = LineRunner(self.codeline)
            print(self.lrun.run())
    def outputans(self) -> str:
        return '\n'.join(self.anslist)

# codes = """space start
# a = 3
# out a
# var b = a + 2
# out 'az'+(str int (str a+b)+'6')+'az'
# c = int (in '请输入:')
# out a+c
# del a
# out a
# del b
# del c
# space end"""

# x = input('选项:\n1.先输入再编译。（同时运行）\n2.运行的同时编译（逐行运行）\n>>')
# if x == '1':
#     print('正在读入')
#     blockrunner = BlockRunner(codes)
#     print('读入成功，开始编译与运行')
#     blockrunner.runcode()
#     print('编译成功，运行结果已存储')
#     print('输出运行结果。\n-------------------')
#     print(blockrunner.outputans())
# else:
#     print('正在读入')
#     blockrunner = BlockRunner(codes)
#     print('读入成功，开始运行。\n-------------------')
#     blockrunner.quickruncode()
#     print('运行完毕。')

print('输入“help /”即可查看教程')
while runnerstatu=='good':
    cmd = input('ins>>')
    linerunner = LineRunner(cmd)
    answer = linerunner.run()
    print(answer)
print('runnerstatu',runnerstatu)
print('exited.')
print('over all.')