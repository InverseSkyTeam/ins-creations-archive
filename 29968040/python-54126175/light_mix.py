from numba import jit, prange
import numpy as np


@jit(nopython=True, fastmath=True, looplift=True)
def light_mix(screen, light_buffer):
    for x in prange(screen.shape[0]):
        for y in prange(screen.shape[1]):
            screen[x, y, 0] = min(screen[x, y, 0] * light_buffer[x, y, 0], 255)
            screen[x, y, 1] = min(screen[x, y, 1] * light_buffer[x, y, 1], 255)
            screen[x, y, 2] = min(screen[x, y, 2] * light_buffer[x, y, 2], 255)
