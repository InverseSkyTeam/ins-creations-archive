print('离1.0版，共完善出6个bug，1个可能被举报现象，总版本2.0.21')
print('这是小轩的宇宙病毒库2.02，看我源码，import Virus，可导出库，你可以用，看作品介绍')
print('关注我，看我个人主页，如果你不喜欢这个，你可以看我的游戏，应用')
print('中文库下期解释，这期放源码')
input('\033[1;31m⚠警告 回车继续，如继续，则代表您承担所有责任，我们绝不负责，不举报，不求赞，只求看！（当然，你也可以大气地赞！如果赞的话先赞再回车，不然你还有一次机会，再不然就可能赞不到就被黑）\033[0m')
print('注意，关机则关闭所有假"病毒"（如开多窗口）,不是真的病毒，直供娱乐用！可以到你朋友家试！')
print('Virus.help()查看帮助，如下\n\n\n\n\n')
import Virus
Virus.help()
print('\n'*5)
a = input('现在可以立即体验：0.不要黑我（保命） 1.程序  2.关机  3.死机（黑屏）  4.开C盘 5.休眠电脑 6.打开小轩个人主页10次 7.打开cmd20次 8.完蛋 9.打开cmd1000次（不要选，99%爆炸）')
if a == '1':
    Virus.viru.Vmain()
if a == '2':
    Virus.viru.shut()
if a == '3':
    Virus.viru.die_computer()
if a == '4':
    Virus.viru.openC()
if a == '5':
    Virus.viru.nap()
if a == '6':
    Virus.file.https(times=10)
if a == '7':
    Virus.file.cmd(times=20)
if a == '8':
    Virus.中文.cmd系列.完蛋()
if a == '9':
    Virus.file.cmd(times=1000)