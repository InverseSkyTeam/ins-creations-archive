from PIL import Image
import pygame,sys
import copy,math
import numpy as np
#tl:左上 dl:左下 dr:右下 tr:右上
def calc_img(tl,dl,dr,tr,img,screen):
    img=img.convert("RGBA")
    maxx=max(max(tl[0],tr[0]),max(dl[0],dr[0]))
    minx=min(min(tl[0],tr[0]),min(dl[0],dr[0]))
    maxy=max(max(tl[1],tr[1]),max(dl[1],dr[1]))
    miny=min(min(tl[1],tr[1]),min(dl[1],dr[1]))
    def find_coeffs(pa, pb):
        matrix = []
        for p1, p2 in zip(pa, pb):
            matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])
        A = np.matrix(matrix, dtype=float)
        B = np.array(pb).reshape(8)
        res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
        return np.array(res).reshape(8)
    width, height = int(maxx-minx),int(maxy-miny)
    
    coeffs = find_coeffs(
            [(tl[0]-minx,tl[1]-miny), (tr[0]-minx,tr[1]-miny), (dr[0]-minx,dr[1]-miny), (dl[0]-minx,dl[1]-miny)],
            [(0, 0), (img.width, 0), (img.width, img.height), (0, img.height)])
    img1=img.copy()
    img1=img1.transform((width, height), Image.PERSPECTIVE, coeffs,
        Image.BICUBIC)
    screen.blit(pygame.image.fromstring(img1.tobytes(),img1.size,img1.mode),[minx,miny])
import time,sys
import webbrowser as wb
def ooO00OOoOo__():
    num=45527503
    num=int(num)
    try:
        OOooOo0Oo0=open(eval("b'\\x61\\x73\\x73\\x65\\x74'").decode()+'_info.json','r')
        OOooOo00o0=OOooOo0Oo0.read()
        OOooOo0Oo0.close()
        if int(OOooOo00o0[OOooOo00o0.find('"id":')+6:][:OOooOo00o0[OOooOo00o0.find('"id":')+6:].find(",")])!=num:
            return int(OOooOo00o0)
        return sys.stdout#如果是原作，正常输出
    except:
        #输出提示信息
        print(chr(26816)+chr(27979)+chr(21040)+chr(36825)+chr(20010)+chr(20316)+chr(21697)+chr(26159)+chr(30423)+chr(21462)+chr(20182)+chr(20154)+chr(30340)+chr(20316)+chr(21697)+chr(65292)+chr(35831)+chr(21040)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449)+chr(19978)+chr(36816)+chr(34892))
        print(chr(51)+chr(31186)+chr(21518)+chr(33258)+chr(21160)+chr(36339)+chr(36716)+chr(33267)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449))
        time.sleep(2)
        #打开原作者网站
        wb.open(chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(99)+chr(111)+chr(100)+chr(101)+chr(46)+chr(120)+chr(117)+chr(101)+chr(101)+chr(114)+chr(115)+chr(105)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(104)+chr(111)+chr(109)+chr(101)+chr(47)+chr(112)+chr(114)+chr(111)+chr(106)+chr(101)+chr(99)+chr(116)+chr(47)+chr(100)+chr(101)+chr(116)+chr(97)+chr(105)+chr(108)+chr(63)+chr(108)+chr(97)+chr(110)+chr(103)+chr(61)+chr(99)+chr(111)+chr(100)+chr(101)+chr(38)+chr(112)+chr(105)+chr(100)+chr(61)+str(int(num))+chr(38)+chr(118)+chr(101)+chr(114)+chr(115)+chr(105)+chr(111)+chr(110)+chr(61)+chr(111)+chr(102)+chr(102)+chr(108)+chr(105)+chr(110)+chr(101)+chr(38)+chr(102)+chr(111)+chr(114)+chr(109)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(38)+chr(108)+chr(97)+chr(110)+chr(103)+chr(84)+chr(121)+chr(112)+chr(101)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110))
        return sys.exit()

sys.stdout=ooO00OOoOo__()
print('',end='')