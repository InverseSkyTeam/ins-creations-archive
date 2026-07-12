from PIL import Image,ImageTk
from tkinter import filedialog
import tkinter as tk
import time
import sys
import os

class App(object):
    def __init__(self):
        a = tk.Tk()
        self.path = filedialog.askdirectory(parent=a)
        a.destroy()

        self.root = tk.Tk()
        self.root.geometry("500x573")
        self.f1 = tk.Frame(self.root)
        image = Image.open("./files/NoFile.png")
        self.image_tk = ImageTk.PhotoImage(image=image)
        self.button = tk.Button(self.f1,image=self.image_tk,height=500,command=self.next_photo)
        self.button.pack(fill=tk.X)
        self.f1.pack(fill=tk.BOTH)

        image1 = Image.open("./files/left.png")
        self.image1 = ImageTk.PhotoImage(image=image1)
        image2 = Image.open("./files/right.png")
        self.image2 = ImageTk.PhotoImage(image=image2)
        self.f2 = tk.Frame(self.root)
        self.b1 = tk.Button(self.f2,image=self.image1,command=self.last_photo,bd=0).pack(side="left")
        self.b2 = tk.Button(self.f2,image=self.image2,command=self.next_photo,bd=0).pack(side="left")
        self.f3 = tk.Frame(self.f2)
        self.e1 = tk.Entry(self.f3)
        self.e1.grid(row=0)
        self.b2 = tk.Button(self.f3,text='跳转',command=self.page,bd=10).grid(row=1)
        self.f3.pack(side="left")
        self.label = tk.Label(self.f2,text="照片0",bg="lightskyblue",width=8)
        self.label.place(x=440,y=45)
        # self.b1.image = image1
        # self.b2.image = image2
        self.f2.pack(fill=tk.BOTH)
        self.root.protocol("WM_DELETE_WINDOW",self.close)
    
    def run(self):
        self.hhh = self.load()
        self.a = "hhh"
        if self.hhh == 'NoFile':
            self.root.mainloop()
        else:
            while self.a:
                try:
                    if self.pos == -1:
                        self.pos = self.length - 1
                    text = self.list[self.pos]
                    if self.is_image(self.path+"//"+text) == False:
                        self.list.remove(text)
                    if len(self.list) == 0:
                        self.close()
                        self.button["image"] = self.image_tk
                        self.root.protocol("WM_DELETE_WINDOW",self.root.destroy)
                        self.root.mainloop()
                    self.label["text"] = "照片"+str(self.pos)
                    photo = Image.open(self.path+"/"+self.list[self.pos])
                    photo = photo.resize((500,500))
                    img = ImageTk.PhotoImage(photo)
                    self.button["image"] = img
                    self.root.update()
                except:
                    self.pos = 0
                # time.sleep(0.5)
                # self.next_photo()

    def load(self):
        try:
            self.list = os.listdir(self.path)
        except FileNotFoundError:
            os.mkdir("images")
            self.list = os.listdir('./images')
        if len(self.list) == 0:
            self.button["image"] = self.image_tk
            return 'NoFile'
        self.pos = 0
        self.length = len(self.list)
    
    def next_photo(self):
        try:
            self.pos += 1
            Image.open(self.path+"/"+self.list[self.pos])
        except:
            pass
        else:
            photo = Image.open(self.path+"/"+self.list[self.pos])
            photo = photo.resize((500,500))
            img = ImageTk.PhotoImage(photo)
            self.button.config(image=img)
            self.button.update()
    
    def last_photo(self):
        try:
            self.pos -= 1
            Image.open(self.path+"/"+self.list[self.pos])
        except:
            pass
        else:
            photo = Image.open(self.path+"/"+self.list[self.pos])
            photo = photo.resize((500,500))
            img = ImageTk.PhotoImage(photo)
            self.button.config(image=img)
            self.button.update()
    
    def page(self):
        page = self.e1.get()
        try:
            self.pos = int(page)
            Image.open(self.path+"/"+self.list[self.pos])
        except:
            pass
        else:
            photo = Image.open(self.path+"/"+self.list[self.pos])
            photo = photo.resize((500,500))
            img = ImageTk.PhotoImage(photo)
            self.button.config(image=img)
            self.button.update()
    
    def is_image(self,file_path):
        try:
            img = Image.open(file_path)
            img.verify()
            return True
        except:
            return False
    
    def close(self):
        if self.hhh == 'NoFile':
            self.root.destroy()
        else:
            self.a = None

if __name__ == '__main__':
    app = App()
    app.run()
