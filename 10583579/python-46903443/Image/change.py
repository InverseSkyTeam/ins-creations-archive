from PIL import Image
im = Image.open(r"设置.jpg")
width = im.size[0]
height = im.size[1]
awa = Image.new("RGB",(1,1),color=(51,51,51))
for x in range(width):
    for y in range(height):
        n = im.getpixel((x,y))
        if n[0] > 100 and n[1] > 100 and n[2] > 100:
            im.paste(awa,(x,y))
im.save("设置.jpg")
