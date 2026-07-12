from PIL import Image, ImageDraw
import time

w, h = 1000, 700
cx, cy = w/2, h/2
r1 = 150
r2 = 200
rd = r2 - r1

image = Image.new('RGBA',(w,h))
draw = ImageDraw.Draw(image)

for x in range(w):
    for y in range(h):
        delta = round(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5)
        if delta <= r1:
            draw.point((x,y),fill=(0,0,0,0))
        elif delta <= r2:
            alpha = 255 - round((r2 - delta) * 255 / rd)
            draw.point((x,y),fill=(0,0,0,alpha))
        else:
            draw.point((x,y),fill=(0,0,0,255))

image.save('bg.png')
print(time.perf_counter())