import bs4
import math
import numpy as np
from PIL import Image


def calc_trans(x, y, kx, ky, sx, sy):
    deg = math.pi/180
    degkx = deg*kx
    eq1, eq2 = math.cos(degkx), math.sin(degkx)
    return [float(sx*eq1), float(sx*eq2), float(sy*eq2), float(sy*eq1), float(x),
            float(y), float(math.tan(deg*ky-degkx) if kx != ky else 0), float(kx), float(ky)]


def open_image(name):
    name = name[len('IMAGE_REANIM_'):]
    return np.array(Image.open('reanim/'+name[0] + name.lower()[1:] + '.png').convert('RGBA'))


with open('Zombie_football.reanim', 'r') as f:
    data = '<html><head></head><body>' + f.read() + '</body></html>'
    html = bs4.BeautifulSoup(data.replace('\n', ''), 'lxml').body
    anim_data = [[] for i in range(len(html.contents[0].contents)-1)]
    for i, img in enumerate(html.contents):
        name = img.find('name').string
        image = None
        x, y, sx, sy, kx, ky, f = 0, 0, 1, 1, 0, 0, 0
        for j, anim in enumerate(img.contents[1:]):
            x = x if anim.x is None else float(anim.x.string)
            y = y if anim.y is None else float(anim.y.string)
            sx = sx if anim.sx is None else float(anim.sx.string)
            sy = sy if anim.sy is None else float(anim.sy.string)
            kx = kx if anim.kx is None else float(anim.kx.string)
            ky = ky if anim.ky is None else float(anim.ky.string)
            f = f if anim.f is None else int(anim.f.string)
            image = image if anim.i is None else open_image(anim.i.string)
            if f == 0 and image is not None:
                anim_data[j].append([image, ]+calc_trans(x, y, kx, ky, sx, sy))

