#导库
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox as msg
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2docx import Converter
import pdfplumber
import pandas as pd
import os
import fitz
from os.path import abspath, dirname


def get_file_name(dir_path):
    file_list = [os.path.join(dirpath, filesname) \
                 for dirpath, dirs, files in os.walk(dir_path) \
                 for filesname in files]
    return file_list

def merge_pdf(target,pdf):
    output = PdfFileWriter()
    file_list = get_file_name(pdf)
    for pdf_file in file_list:
        # 读取PDF文件
        input = PdfFileReader(open(pdf_file, "rb"))
        # 获得源PDF文件中页面总数
        pageCount = input.getNumPages()
        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.addPage(input.getPage(iPage))
    # 写入到目标PDF文件
    with open(os.path.join(target, "target.pdf"), "wb") as outputfile:
        output.write(outputfile)

def mergepdf():
    global input1,input2
    merge_pdf(input2.get(),input1.get())
    msg.showinfo("完成","合并完成!")

def pdfs2docxs(pdfpath,docxpath):
    for i in os.listdir(pdfpath):
        namelist = i.split('.')
        if namelist[-1] == 'pdf':
            name = ''.join(namelist[:-1])
            pdf = pdfpath + i
            doc = docxpath + name + '.docx'
            cv = Converter(pdf)
            cv.convert(doc) # 默认参数start=0, end=None
            cv.close()

def pdf2doc():
    global input1,input2
    pdfs2docxs(input1.get(),input2.get())
    msg.showinfo('完成','转换完成!')

def extracettext(pdfpath,targetpath):
    for i in os.listdir(pdfpath):
        namelist = i.split('.')
        if namelist[-1] == 'pdf':
            name = ''.join(namelist[:-1])
            pdfnm = pdfpath + i
            pdf = pdfplumber.open(pdfnm)
            txt = ''
            for x in pdf.pages:
                txt = txt + "\n" + x.extract_text()
            with open(targetpath + name + '.txt','w') as file:
                file.write(txt)

def extext():
    global input1,input2
    extracettext(input1,input2)
    msg.showinfo('完成','提取完成!')

def extable():
    global input1,input2
    extracettable(input1,input2)
    msg.showinfo('完成','提取完成!')

def eximg():
    global input1,input2
    extracetimg(input1,input2)
    msg.showinfo('完成','提取完成!')

def extracettable(pdfpath,targetpath):
    for i in os.listdir(pdfpath):
        namelist = i.split('.')
        if namelist[-1] == 'pdf':
            name = ''.join(namelist[:-1])
            pdfnm = pdfpath + i
            pdf = pdfplumber.open(pdfnm)
            for x in pdf.pages:
                table = x.extract_table()
                # 将列表转为df
                table_df = pd.DataFrame(table[1:],columns=table[0])
                # 保存excel
                table_df.to_excel(targetpath + name + '.xlsx')

def muExtractImages(pdf,picPath):
    pdfsplit = os.path.split(pdf)   #分离出文件名和路径
    pdfname = pdfsplit[-1]  #获取文件名
    pdfsplit1 = os.path.splitext(pdfname)
    pdfname1 = pdfsplit1[0]   #获取不带扩展名的文件名
    
    #print(pdfsplit)
    #print(pdfname)
    #print(pdfname1)
    # 打开pdf，打印PDF的相关信息
    doc = fitz.open(pdf)
    # 图片计数
    imgcount = 0
    lenXREF = doc.xref_length()    #获取pdf文件对象总数
    
    #遍历doc，获取每一页
    for page in doc: 
        try:
            imgcount +=1
            tupleImage = page.get_images()
            lstImage = list(tupleImage)
            xref0 = lstImage[0]    #取第一个元组
            xref1 = list(xref0)     #元组转化为列表
            xref = xref1[0]   #最终取得xref  ok
            img = doc.extract_image(xref)   #获取文件扩展名，图片内容 等信息
            imageFilename = ("%s-%s." % (imgcount, xref) + img["ext"])
            imageFilename = pdfname1 + "_" + imageFilename  #合成最终 的图像的文件名
            imageFilename = os.path.join(picPath, imageFilename)   #合成最终图像完整路径名
            imgout = open(imageFilename, 'wb')   #byte方式新建图片
            imgout.write(img["image"])   #当前提取的图片写入磁盘
            imgout.close
        except:
            continue

def extracetimg(pdfpath,targetpath):
    for i in os.listdir(pdfpath):
        namelist = i.split('.')
        if namelist[-1] == 'pdf':
            name = ''.join(namelist[:-1])
            pdfnm = pdfpath + i
            pt = targetpath + name
            os.mkdir(pt)
            muExtractImages(pdfnm,pt)

#选择文档及目标路径的函数
def choose_doc():
    global docfilename,e
    docfilename =tkinter.filedialog.askdirectory() + "/"
    e.set(docfilename)

def choose_target():
    global targetfilename,e2
    targetfilename =tkinter.filedialog.askdirectory() + "/"
    e2.set(targetfilename)

def main():
    root = ttk.Window(themename="darkly")
    root.title("PDF工具集")
    root.geometry("600x200")

    label1 = ttk.Label(root,text="PDF文件夹路径")
    label1.place(x = 10,y = 20)
    e = ttk.StringVar()
    input1 = ttk.Entry(root,width=35,textvariable=e)
    input1.place(x = 130,y = 20)
    button1 = ttk.Button(root,width = 5,text = "浏览",command=choose_doc)
    button1.place(x= 465,y = 20)

    label2 = ttk.Label(root,text="目标文件夹路径")
    label2.place(x = 10,y = 80)
    e2 = ttk.StringVar()
    input2 = ttk.Entry(root,width=35,textvariable=e2)
    input2.place(x = 130,y = 80)
    button2 = ttk.Button(root,width = 5,text = "浏览",command=choose_target)
    button2.place(x= 465,y = 80)

    button4merge = ttk.Button(root,text = "合并PDF",width = 7,command=mergepdf)
    button4merge.place(x = 50,y = 150)

    button4docx = ttk.Button(root,text = "转为DOCX",width = 8,command=pdf2doc)
    button4docx.place(x = 160,y = 150)

    button4text = ttk.Button(root,text = "提取文字",width = 8,command=extext)
    button4text.place(x = 270,y = 150)

    button4table = ttk.Button(root,text = "提取表格",width = 8,command=extable)
    button4table.place(x = 380,y = 150)

    button4img = ttk.Button(root,text = "提取图片",width = 8,command=eximg)
    button4img.place(x = 490,y = 150)

    root.mainloop()