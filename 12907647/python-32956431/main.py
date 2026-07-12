import uiautomation as auto
import subprocess
# 设置全局搜索超时时间为1秒
auto.uiautomation.SetGlobalSearchTimeout(1)

# 查找notepad
note = auto.WindowControl(
    searchDepth=1, ClassName='Notepad', RegexName='.* - 记事本')
if not auto.WaitForExist(note, 0.1):
    subprocess.Popen('notepad')
sw, sh = auto.GetScreenSize()
note.MoveWindow(sw // 10, sh // 10, sw // 2, sh // 2)
note.SetActive()
note.SetTopmost()
text = """Windows中GUI自动化的三种技术：Windows API, MSAA - Microsoft Active Accessibility, UIAutomation
用脚本语言AutoIT实现自动化就是第一种技术Windows API, 查找窗口句柄实现的。
用工具Spy++查看程序，如果Spy++能识别程序窗口中的控件就能用这种技术。
python的UI自动化测试模块 pywinauto，也是用这种技术实现的(现在pywinauto也支持UIAutomation了)。 
但Windows API实现的自动化不支持WPF程序、Windows 8中的Metro程序，因为它们的控件都是自绘出来的，没有句柄的概念。
用UIAutomation实现的自动化支持微软提供的各种界面开发框架，如Win32, MFC, Windows Forms, WPF, Metro App, IE。
Qt, Firefox, Chrome实现了UI Automation Provider，也支持UIAutomation.

tip:
Win10系统下应该使用64位Python运行本程序，32位进程无法正确获取一些控件的边界坐标。
详见：https://github.com/microsoft/accessibility-insights-windows/issues/1122
"""
edit = note.EditControl()
edit.Click(waitTime=0)
edit.GetValuePattern().SetValue('你好')
edit.SendKeys('{Ctrl}{End}{Enter}下面开始演示{! 3}{ENTER}', 0.2, 0)
edit.SendKeys(text)
edit.SendKeys('{Enter 3}0123456789{Enter}', waitTime=0)
edit.SendKeys('ABCDEFGHIJKLMNOPQRSTUVWXYZ{ENTER}', waitTime=0)
edit.SendKeys('abcdefghijklmnopqrstuvwxyz{ENTER}', waitTime=0)
edit.SendKeys('`~!@#$%^&*()-_=+{ENTER}', waitTime=0)
edit.SendKeys('[]{{}{}}\|;:\'",<.>/?{ENTER}', waitTime=0)
edit.SendKeys('™®①②③④⑤⑥⑦⑧⑨⑩§№☆★○●◎◇◆□℃‰€■△▲※→←↑↓〓¤°＃＆＠＼＾＿―♂♀')
edit.SendKeys("{ENTER}{CTRL}a")
note.CaptureToImage('Notepad.png')
# 查找菜单
note.MenuItemControl(Name='格式(O)').Click()
note.MenuItemControl(Name='字体(F)...').Click()
windowFont = note.WindowControl(Name='字体')
font_data = {"字体(F):": "微软雅黑", "字形(Y):": "常规", "大小(S):": "小四"}
for k, v in font_data.items():
    listItem = windowFont.ListControl(
        searchDepth=2, AutomationId='1000', Name=k).ListItemControl(Name=v)
    if listItem.Exists(1):
        listItem.GetScrollItemPattern().ScrollIntoView()
        listItem.Click()
windowFont.SetActive()
combo = windowFont.ComboBoxControl(AutomationId='1140')
combo.Select('中文 GB2312')
windowFont.ButtonControl(Name='确定').Click()
note.SetTopmost(False)
subprocess.Popen('Notepad.png', shell=True)