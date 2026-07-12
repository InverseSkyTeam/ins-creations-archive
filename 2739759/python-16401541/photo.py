#coding=utf-8
import pygame,sys,os
from PIL import Image,ImageFont,ImageDraw
size = (800, 720)
#width =150#设置字符画中每个字符所占的长宽
#height=50
key="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
def get_char(r,g,b,alpha= 255):
    ascii_char = list(key)
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unitcount  = (256.0+1)/length
    return  ascii_char[int(gray/unitcount)]

def superPic(imgname,color=(0,255,0),width=150,height=50,name="output1.png"):
    img  = Image.open(imgname)
    img  = img.resize((width,height),Image.NEAREST)
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*img.getpixel((j,i)),key)
        txt += '\n'
    #print(txt)
    im = Image.new("RGBA",size, (0, 0, 0,0))#设置字符图尺寸与背景颜色
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("simsun.ttc", 10, encoding="utf-8")
    dr.text((10,7.2), txt, font=font, fill=color)
    im.show()
    im.save('C:/'+name)
    photo = name
    return photo

def superTxt(txt,color=(0,255,0),fontSize=200,width=150,height=100,name="output2.png"):
    im = Image.new("RGB", (800,450), (255, 255, 255,0)) #设置字符图尺寸与背景颜色   # 450 100
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("simsun.ttc", fontSize, encoding="utf-8")
    dr.text((10, 5), txt, font=font, fill="#000000")
    #im.show()
    im.save(name)
    imgname = name
    img  = Image.open(imgname)
    img  = img.resize((width,height),Image.NEAREST)
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*img.getpixel((j,i)),key)
        txt += '\n'
    im = Image.new("RGBA", size, (0, 0, 0,0))#设置字符图尺寸与背景颜色
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("simsun.ttc", 10, encoding="utf-8")
    dr.text((10, 7.2), txt, font=font, fill=color)
    im.show()
    im.save('C:/'+name)
    photo = name
    return photo



# ----------------- 调用生成字符画

# txt ="SOS"
# superTxt(txt)
# ,color=(0,255,0),fontSize=200,width=150,height=100,name="66.png"



# superPic("44.jpg")
# ,color=(0,255,0),width=150,height=50,name="55.png"
