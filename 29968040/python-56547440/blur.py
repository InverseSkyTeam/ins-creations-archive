from numba import njit
import numpy as np
import math


def box_blur(surface, radius, repeat_edge_pixels=True, dest_surface=None):
    return blur(surface, dest_surface, radius, repeat_edge_pixels, 'b')


def gaussian_blur(surface, radius, repeat_edge_pixels=True, dest_surface=None):
    return blur(surface, dest_surface, radius, repeat_edge_pixels, 'g')


def blur(srcobj, dstobj, radius, repeat, algorithm):
    if radius < 0:
        raise ValueError('The radius should not be less than zero.')

    src = srcobj
    '''if (src->format->palette) {
        return RAISE(PyExc_ValueError, "Indexed surfaces cannot be blurred.");
    }'''
    if not dstobj:
        retsurf = src.copy()
        if not retsurf:
            return None
    else:
        retsurf = dstobj

    if retsurf.get_size() != src.get_size():
        raise ValueError('Destination surface not the same size.')
    if retsurf.get_width() == 0 or retsurf.get_height() == 0:
        return retsurf

    '''Uint8 *ret_start = retsurf->pixels;
    Uint8 *ret_end = ret_start + retsurf->h * retsurf->pitch;
    Uint8 *src_start = src->pixels;
    Uint8 *src_end = src_start + src->h * src->pitch;
    if ((ret_start <= src_start && ret_end >= src_start) ||
        (src_start <= ret_start && src_end >= ret_start)) {
        return RAISE(
            PyExc_ValueError,
            "Blur routines do not support dest_surfaces that share pixels "
            "with the source surface. Likely the surfaces are the same, one "
            "of them is a subsurface, or they are sharing the same buffer.");
    }'''

    if src.get_bytesize() != retsurf.get_bytesize():
        raise ValueError('Source and destination surfaces need the same format.')
    if radius > min(src.get_size()):
        radius = min(src.get_size()) - 1

    srcpx = np.array(src.get_view('0'), copy=False)
    dstpx = np.array(retsurf.get_view('0'), copy=False)
    nb = src.get_bytesize()
    w, h = src.get_size()
    src_pitch, dst_pitch = src.get_pitch(), retsurf.get_pitch()

    if algorithm == 'b':
        _box_blur(radius, repeat, w, h, srcpx, dstpx, nb, src_pitch, dst_pitch)
    elif algorithm == 'g':
        _gaussian_blur(radius, repeat, w, h, srcpx, dstpx, nb, src_pitch, dst_pitch)
    return retsurf


@njit('void(int32, boolean, int32, int32, uint8[:], uint8[:], uint8, int32, int32)', looplift=True)
def _box_blur(radius, repeat, w, h, srcpx, dstpx, nb, src_pitch, dst_pitch):
    buf = np.empty(dst_pitch, dtype=np.uint32)
    sum_v = np.zeros(dst_pitch, dtype=np.uint32)
    sum_h = np.empty(nb, dtype=np.uint32)

    for y in range(radius + 1):
        sum_v += srcpx[src_pitch * y: src_pitch * y + dst_pitch]
    if repeat:
        sum_v += (srcpx[:dst_pitch] * radius).astype(np.uint32)
    _rad = 1 / (radius * 2 + 1)
    for y in range(h):
        for i in range(dst_pitch):
            buf[i] = sum_v[i] * _rad

            # update vertical sum
            if y - radius >= 0:
                sum_v[i] -= srcpx[src_pitch * (y - radius) + i]
            elif repeat:
                sum_v[i] -= srcpx[i]
            if y + radius + 1 < h:
                sum_v[i] += srcpx[src_pitch * (y + radius + 1) + i]
            elif repeat:
                sum_v[i] += srcpx[src_pitch * (h - 1) + i]

        sum_h.fill(0)
        for color in range(nb):
            sum_h[color] += buf[color: (radius + 1) * nb + color: nb].sum()
        if repeat:
            for color in range(nb):
                sum_h[color] += buf[color] * radius
        for color in range(nb):
            nb_x = color
            for x in range(w):
                dstpx[dst_pitch * y + nb_x] = sum_h[color] * _rad

                # update horizontal sum
                if x - radius >= 0:
                    sum_h[color] -= buf[nb_x - radius * nb]
                elif repeat:
                    sum_h[color] -= buf[color]
                if x + radius + 1 < w:
                    sum_h[color] += buf[nb_x + radius * nb + nb]
                elif repeat:
                    sum_h[color] += buf[(w - 1) * nb]
                nb_x += nb


@njit('void(int32, boolean, int32, int32, uint8[:], uint8[:], uint8, int32, int32)', looplift=True)
def _gaussian_blur(sigma, repeat, w, h, srcpx, dstpx, nb, src_pitch, dst_pitch):
    kernel_radius = sigma * 2
    buf = np.zeros(dst_pitch, dtype=np.float32)
    buf2 = np.zeros(dst_pitch, dtype=np.float32)
    lut = np.empty(kernel_radius + 1, dtype=np.float32)
    lut_sum = 0.0

    for i in range(kernel_radius + 1):
        # Gaussian function
        lut[i] = math.exp(-float(i * i) / (2.0 * sigma * sigma))
        lut_sum += lut[i] * 2
    lut_sum -= lut[0]
    lut /= lut_sum

    for y in range(h):
        for j in range(-kernel_radius, kernel_radius + 1):
            if 0 <= y + j < h:
                buf += srcpx[src_pitch * (y + j): src_pitch * (y + j) + dst_pitch] * lut[abs(j)]
            elif repeat:
                if y + j < 0:
                    buf += srcpx[:dst_pitch] * lut[abs(j)]
                else:
                    buf += srcpx[src_pitch * (h - 1): src_pitch * (h - 1) + dst_pitch] * lut[abs(j)]

        for color in range(nb):
            for j in range(-kernel_radius, kernel_radius + 1):
                nb_x = color
                for x in range(w):
                    if 0 <= x + j < w:
                        buf2[nb_x] += buf[nb_x + nb * j] * lut[abs(j)]
                    elif repeat:
                        if x + j < 0:
                            buf2[nb_x] += buf[color] * lut[abs(j)]
                        else:
                            buf2[nb_x] += buf[nb * (w - 1) + color] * lut[abs(j)]
                    nb_x += nb
        dstpx[dst_pitch * y: dst_pitch * y + dst_pitch] = buf2.astype(np.uint8)
        buf.fill(0.0)
        buf2.fill(0.0)
