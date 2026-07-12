import bs4
import math
import numpy as np
from PIL import Image
from multiprocessing.dummy import Pool
import time


def calc_trans(x, y, kx, ky, sx, sy):
    deg = math.pi / 180
    degkx = deg * kx
    degky = deg * ky
    a = sx * math.cos(degkx)
    b = sx * math.sin(degkx)
    c = -sy * math.sin(degky)
    d = sy * math.cos(degky)
    return [a, b, c, d, x, y]


def open_image(name):
    name = name[len('IMAGE_REANIM_'):]
    image = np.array(Image.open('Reanim/' + name[0] + name.lower()[1:] + '.png').convert('RGBA'))
    return image


def open_reanim(file_name):
    a1 = time.time()
    if '.reanim' not in file_name:
        file_name += '.reanim'
    with open(file_name, 'r') as f:
        data = '<html><head></head><body>' + f.read() + '</body></html>'
        html = bs4.BeautifulSoup(data.replace('\n', ''), 'lxml').body
        anim_data = [[] for i in range(len(html.contents[3].contents)-1)]
        act_data = {}
        act_name = []
        for i, img in enumerate(html.contents[1:]):
            name = img.find('name').string
            image = None
            x, y, sx, sy, kx, ky, f, a = 0, 0, 1, 1, 0, 0, 0, 1
            for j, anim in enumerate(img.contents[1:]):
                x = x if anim.x is None else float(anim.x.string)
                y = y if anim.y is None else float(anim.y.string)
                sx = sx if anim.sx is None else float(anim.sx.string)
                sy = sy if anim.sy is None else float(anim.sy.string)
                kx = kx if anim.kx is None else float(anim.kx.string)
                ky = ky if anim.ky is None else float(anim.ky.string)
                f = f if anim.f is None else int(anim.f.string)
                a = a if anim.a is None else float(anim.a.string)
                image = image if anim.i is None else open_image(anim.i.string)
                if f == 0 and image is not None:
                    anim_data[j].append([image, ]+calc_trans(x, y, kx, ky, sx, sy)+[name, a])
                if f == 0 and image is None and 'anim_' in name:
                    if name not in act_data:
                        act_data[name] = [j, None]
                        act_name.append(name)
                    else:
                        act_data[name][1] = j
        act_name = sorted(act_name, key=lambda a_name: act_data[a_name][0])
    b = time.time()
    print(f'加载{file_name}完成，用时{b-a1}s')
    return anim_data, act_data, act_name


def open_reanims(file_names):
    reanims = {}
    a = time.time()
    pool = Pool(len(file_names))
    res = pool.map(open_reanim, file_names)
    b = time.time()
    print(f'全部加载完成，用时{b-a}s')
    for i, file_name in enumerate(file_names):
        reanims[file_name] = res[i]
    return reanims
