from render import render, Model
print("运行前需要十秒左右的初始化，请耐心等待")
# you can export the *.obj format model data from blender
render(
    Model("res/axe.obj", texture_filename="res/axe.tga"),
    height=4000,
    width=4000,
    filename="axe.png",
)
from PIL import Image
image = Image.open("axe.png")
image.show()
