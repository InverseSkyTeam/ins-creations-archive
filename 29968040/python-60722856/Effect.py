import numpy as np
import pygame
import math


class Effect:
    def transform_image(img, mosaic, pixelate, whirl, fisheye):
        w, h = img.get_size()
        dst_sf = pygame.Surface((w, h), pygame.SRCALPHA).convert_alpha()
        effects = ((mosaic != 0) * (1 << 4)) | ((pixelate != 0) * (1 << 3)) | ((whirl != 0) * (1 << 2)) | ((fisheye != 0) * (1 << 1))
        fisheye = max(0, (fisheye + 100) / 100)
        mosaic = max(1, min(round((abs(mosaic) + 10) / 10), 512))
        pixelate = abs(pixelate) / 10
        whirl = -whirl * math.pi / 180
        
        xs, ys = np.mgrid[:w, :h]
        index = ys * w + xs
        xs, ys = xs / w, ys / h
        
        if (effects & (1 << 4)) != 0:
            xs = mosaic * xs % 1
            ys = mosaic * ys % 1

        if (effects & (1 << 3)) != 0:
            texelX = w / pixelate
            texelY = h / pixelate
            xs = (np.floor(xs * texelX) + 0.5) / texelX
            ys = (np.floor(ys * texelY) + 0.5) / texelY
 
        if (effects & (1 << 2)) != 0:
            offsetX = xs - 0.5
            offsetY = ys - 0.5
            offsetMagnitude = np.sqrt(offsetX ** 2 + offsetY ** 2)
            whirlFactor = np.maximum(1.0 - (offsetMagnitude * 2), 0.0)
            whirlActual = whirl * whirlFactor * whirlFactor
            sinWhirl = np.sin(whirlActual)
            cosWhirl = np.cos(whirlActual)
            rot1 = cosWhirl
            rot2 = -sinWhirl
            rot3 = sinWhirl
            rot4 = cosWhirl

            xs = (rot1 * offsetX) + (rot3 * offsetY) + 0.5
            ys = (rot2 * offsetX) + (rot4 * offsetY) + 0.5

        if (effects & (1 << 1)) != 0:
            vX = (xs - 0.5) * 2
            vY = (ys - 0.5) * 2
            vLength = np.sqrt((vX * vX) + (vY * vY))
            r = (np.minimum(vLength, 1) ** fisheye) * np.maximum(vLength, 1)
            unitX = vX / vLength
            unitY = vY / vLength
            xs = 0.5 + (r * unitX / 2)
            ys = 0.5 + (r * unitY / 2)
        xs = np.clip((xs * w).astype(np.uint32), 0, w-1)
        ys = np.clip((ys * h).astype(np.uint32), 0, h-1)
        src = np.array(img.get_view("1"), copy=False)
        dst = np.array(dst_sf.get_view("1"), copy=False)
        dst[index] = src[ys * w + xs]
        return dst_sf
    
    @staticmethod
    def transform_color(image, color):
        color = 1 + ((color / 200) % 1)
        new_sf = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        new_sf.blit(image, (0, 0))
        rgb_sf = pygame.surfarray.pixels3d(new_sf)
        rgb = rgb_sf.astype(np.float64)
        r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    
        maxv = np.maximum(np.maximum(r, g), b)
        minv = np.minimum(np.minimum(r, g), b)

        diff = maxv - minv
    
        h = np.full_like(maxv, color)
        mask = (diff != 0)
        
        color_select = [(maxv == r) & mask, (maxv == g) & mask, (maxv == b) & mask]
        minuend = np.select(color_select, [g, b, r])
        subtrahend = np.select(color_select, [b, r, g])
        add_num = np.select(color_select, [360, 120, 240])
        h[mask] += ((60 * ((minuend[mask] - subtrahend[mask]) / diff[mask]) + add_num[mask]) % 360) / 360

        s = np.zeros_like(maxv)
        tmp = maxv != 0
        s[tmp] = diff[tmp] / maxv[tmp]
    
        min_V = 0.11 / 2.0 * 255.0
        min_S = 0.09
        min_max_select = [maxv < min_V, s < min_S]
        h[min_max_select[0] | min_max_select[1]] = color
        s = np.select(min_max_select, [1, min_S], default=s)
        maxv[min_max_select[0]] = min_V

        h %= 1
        h *= 6
        i = h.astype(np.uint8)
        f = h - i
        s_v = s * maxv
        s_v_f = s_v * f
        p = maxv - s_v
        q = maxv - s_v_f
        t = p + s_v_f
    
        select_cond = [i == 0, i == 1, i == 2, i == 3, i == 4, i == 5]
        r = np.select(select_cond, [maxv,    q,    p,    p,    t, maxv])
        g = np.select(select_cond, [   t, maxv, maxv,    q,    p,    p])
        b = np.select(select_cond, [   p,    p,    t, maxv, maxv,    q])
    
        rgb_sf[..., 0] = r
        rgb_sf[..., 1] = g
        rgb_sf[..., 2] = b
        return new_sf
