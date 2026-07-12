from numba import jit, uint32


u32 = uint32


@jit(nopython=True, fastmath=True, cache=True, looplift=True)
def _render(screen, image, w, h, args, alpha):
    x1, y1 = round(args[4]), round(args[5])
    x2, y2 = round(args[2] * h + args[4]), round(args[3] * h + args[5])
    x3, y3 = round(args[0] * w + args[2] * h + args[4]), round(args[1] * w + args[3] * h + args[5])
    x4, y4 = round(args[0] * w + args[4]), round(args[1] * w + args[5])
    
    d = 1 / (args[0] * args[3] - args[1] * args[2])
    m0 = args[3] * d
    m1 = -args[1] * d
    m2 = -args[2] * d
    m3 = args[0] * d
    m4 = d * (args[2] * args[5] - args[3] * args[4])
    m5 = d * (args[1] * args[4] - args[0] * args[5])
    
    bound_sx = max(min(x1, x2, x3, x4), 0)
    bound_ex = min(max(x1, x2, x3, x4), screen.shape[0])
    bound_sy = max(min(y1, y2, y3, y4), 0)
    bound_ey = min(max(y1, y2, y3, y4), screen.shape[1])

    __src_x = (bound_sx - 1) * m0 + (bound_sy - 1) * m2 + m4
    __src_y = (bound_sx - 1) * m1 + (bound_sy - 1) * m3 + m5
    for x in range(bound_sx, bound_ex):
        __src_x += m0
        __src_y += m1
        _src_x = __src_x
        _src_y = __src_y
        for y in range(bound_sy, bound_ey):
            _src_x += m2
            _src_y += m3
            src_x = int(_src_x + 0.5) if _src_x > 0 else int(_src_x - 0.5)
            src_y = int(_src_y + 0.5) if _src_y > 0 else int(_src_y - 0.5)
            if src_x < 0 or src_x >= w or src_y < 0 or src_y >= h:
                continue
            dstp = u32(screen[x, y])
            srcp = u32(image[src_x * h + src_y])
            mn = u32((srcp >> 24) * alpha) + 1
            mp = 257 - mn
            screen[x, y] = (((((srcp & u32(0x00FF00FF)) * mn)+((dstp & u32(0x00FF00FF)) * mp)) & u32(0xFF00FF00)) +
                            ((((srcp & u32(0x0000FF00)) * mn)+((dstp & u32(0x0000FF00)) * mp)) & u32(0x00FF0000))) >> 8


@jit(nopython=True, fastmath=True, cache=True)
def render(screen, texture, texture_index, texture_size, x, y, args):
    alpha = args[0]
    arg = args[1], args[2], args[3], args[4], args[5] + x, args[6] + y
    index = texture_index[int(args[7])]
    w, h = texture_size[int(args[7])]
    image = texture[index: index + w * h]
    _render(screen, image, w, h, arg, alpha)
