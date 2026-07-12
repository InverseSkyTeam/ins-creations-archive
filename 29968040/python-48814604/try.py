from render import render, Model

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
