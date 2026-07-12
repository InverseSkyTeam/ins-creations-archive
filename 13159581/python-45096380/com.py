from pgzrun import *
import c
import d
import e

WIDTH = 700
HEIGHT = 500

bg = Actor("bg3.png")
cc = Actor("cc.png",[50,50])
dd = Actor("dd.png",[150,50])
ee = Actor("ee.png",[250,50])

def draw():
    bg.draw()
    cc.draw()
    dd.draw()
    ee.draw()

def on_mouse_down(pos,button):
    if button == mouse.RIGHT:
        pass
    if button == mouse.LEFT:
        if cc.collidepoint(pos):
            c.main()
        if dd.collidepoint(pos):
            d.main()
        if ee.collidepoint(pos):
            e.main()

go()
