from time import sleep
from random import randint as r

r'''
\033(\x1b)函数颜色代码

\033[0m 关闭所有属性

\033[1m 设置高亮度高
\033[2m 设置高亮度低
\033[3m 斜体
\033[4m 下划线
\033[5m 闪烁
\033[6m 无效果
\033[7m 反显
\033[8m 消隐
\033[22m 设置高亮度中（默认）
\033[23m 关闭斜体
\033[24m 关闭下划线
\033[25m 关闭闪烁
\033[26m 无效果
\033[27m 关闭反显
\033[28m 关闭消隐

\033[3xm 设置字体色（x=0~7）
\033[4xm 设置背景色（x=0~7）
\033[38;2;R;G;Bm 字体RGB颜色
\033[48;2;R;G;Bm 背景RGB颜色
\033[9xm 调配颜色

\033[nA 光标上移n行 
\033[nB 光标下移n行
\033[nC 光标右移n行
\033[nD 光标左移n行
\033[y;xH设置光标位置
\033[s 保存光标位置 
\033[u 恢复光标位置

\033[?25l 隐藏光标
\033[?25h 显示光标

\033[xJ 清屏x个偏离单位
\033[K 清除从光标到行尾的内容
'''

string3D0= r'''                      
  ___________         
 |\   _____  \        
 \ \  \    \  \       
  \ \  \    \  \      
   \ \  \    \  \     
    \ \  \    \  \    
     \ \  \    \  \   
      \ \  \    \  \  
       \ \  \____&  \ 
        \ \__________\
         \|__________|
                      '''

string3D2= r'''                      
  ___________         
 |\______    \        
 \|_____|\    \       
        \ \    \      
      ___&_&    \     
     |\   _______\    
     \ \  \______|    
      \ \  \          
       \ \  \________ 
        \ \__________\
         \|__________|
                      '''

string3D3= r'''                      
  ___________         
 |\______    \        
 \|_____|\    \       
        \ \    \      
      ___&_&    \     
     |\________  \    
     \|_______|\  \   
              \ \  \  
          _____&_&  \ 
         |\__________\
         \|__________|
                      '''

dic = {
    0: [
        string3D0.replace('&','\\'),  # 普通
        '\033[3m'+string3D0.replace('&','\\')+'\033[23m',  # 融斜
        string3D0.replace('&','\033[4m\\\033[24m'),  # 补完
        ],
    2: [
        string3D2.replace('&','\\'),  # 普通
        '\033[3m'+string3D2.replace('&','\\')+'\033[23m',  # 融斜
        string3D2.replace('&','\033[4m\\\033[24m'),  # 补完
        ],
    3: [
        string3D3.replace('&','\\'),  # 普通
        '\033[3m'+string3D3.replace('&','\\')+'\033[23m',  # 融斜
        string3D3.replace('&','\033[4m\\\033[24m'),  # 补完
        ],
}

class Integer:
    def __init__(self,year):
        self.year = [int(i) for i in list(str(year))]
        self.fontsize = 13
        self.string = [['' for i in range(self.fontsize)] for i in (1,2,3)]
        for mode in range(3):
            for y in self.year:
                char = dic[y][mode].split('\n')
                for i in range(self.fontsize):
                    self.string[mode][i] += char[i]
        for mode in range(3):
            self.string[mode] = '\n'.join(self.string[mode])

def cs():
    print('\033[30A')
def background(color):
    print('\033[4'+str(color)+'m',end='')
def closecolor():
    print('\033[0m',end='')
def beautiout(string,delay=0.02):
    for each in string:
        print(each,sep='',end='',flush=True)
        sleep(delay)
    print()

cs()
i2022 = Integer('2022')
i2023 = Integer('2023')

# 正片开始6 #
background(0)
print(i2022.string[0])
closecolor()
print('这是一个过去...')
cs()
sleep(2)
beautiout((' '*100+'\n')*20,delay=0)
cs()
background(0)
beautiout(i2023.string[1])
closecolor()
cs()
background(2)
print('这，则是新的开始')
closecolor()
cs()

background(0)
for tt in range(20):
    for i in (1,0,2):
        print(i2023.string[i])
        sleep(0.05)
        cs()

print('\033[1m',end='')
background(0)
cs()
for tt in range(20):
    print('\033[3'+str(r(0,7))+'m',end='')
    print(i2023.string[2])
    cs()
    sleep(0.1)
print('\033[32m',end='')
print(i2023.string[2])
cs()
sleep(1)
closecolor()
background(2)
cs()
print(i2023.string[2])
closecolor()
print('\n\n')
print('2023 终端3D')
print('春节快乐！新年快乐！新的一年，新的开始！感谢你的观看！喜欢可以三连')
print('快送给你的家人们吧！（下面的蓝色字体是真的代码运行结束，不信看按钮）')
print('Copyright.(C)INS 逆天小轩 2023 3D.')
print('All right released.')
print('\n\n\033[1;34m-*本程序解释运行完毕，版权小轩所有*-\033[?25l\033[13A\033[8m')