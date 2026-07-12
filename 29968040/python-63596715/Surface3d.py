import numpy as np
from PIL import Image
import pygame


def find_coeffs(pa, pb):
    matrix = [
        [pa[0][0], pa[0][1], 1, 0, 0, 0, -pb[0][0]*pa[0][0], -pb[0][0]*pa[0][1]], 
        [0, 0, 0, pa[0][0], pa[0][1], 1, -pb[0][1]*pa[0][0], -pb[0][1]*pa[0][1]],
        [pa[1][0], pa[1][1], 1, 0, 0, 0, -pb[1][0]*pa[1][0], -pb[1][0]*pa[1][1]],
        [0, 0, 0, pa[1][0], pa[1][1], 1, -pb[1][1]*pa[1][0], -pb[1][1]*pa[1][1]],
        [pa[2][0], pa[2][1], 1, 0, 0, 0, -pb[2][0]*pa[2][0], -pb[2][0]*pa[2][1]],
        [0, 0, 0, pa[2][0], pa[2][1], 1, -pb[2][1]*pa[2][0], -pb[2][1]*pa[2][1]],
        [pa[3][0], pa[3][1], 1, 0, 0, 0, -pb[3][0]*pa[3][0], -pb[3][0]*pa[3][1]],
        [0, 0, 0, pa[3][0], pa[3][1], 1, -pb[3][1]*pa[3][0], -pb[3][1]*pa[3][1]],
    ]
    A = np.matrix(matrix, dtype=float)
    B = np.array(pb).reshape(8)
    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.array(res).reshape(8)


class Resampling:
    NEAREST = Image.NEAREST if hasattr(Image, 'NEAREST') else Image.Resampling.NEAREST
    BILINEAR = Image.BILINEAR if hasattr(Image, 'BILINEAR') else Image.Resampling.BILINEAR
    BICUBIC = Image.BICUBIC if hasattr(Image, 'BICUBIC') else Image.Resampling.BICUBIC


class Surface3d:
    PERSPECTIVE = Image.PERSPECTIVE if hasattr(Image, 'PERSPECTIVE') else Image.Transform.PERSPECTIVE
    
    def __init__(self, surface):
        self.resampling = Resampling.NEAREST
        
        self.surface = surface.convert_alpha()
        self.pil_image = Image.frombytes('RGBA', surface.get_size(), pygame.image.tobytes(self.surface, 'RGBA'))

    def change_surface(self, surface):
        self.surface = surface.convert_alpha()
        self.pil_image = Image.frombytes('RGBA', surface.get_size(), pygame.image.tobytes(self.surface, 'RGBA'))

    def render(self, screen, border):
        tl,dl,dr,tr = border
        img = self.pil_image
        maxx = max(tl[0], tr[0], dl[0], dr[0])
        minx = min(tl[0], tr[0], dl[0], dr[0])
        maxy = max(tl[1], tr[1], dl[1], dr[1])
        miny = min(tl[1], tr[1], dl[1], dr[1])
        if maxx - minx == 0 or maxy - miny == 0:
            return
        width, height = int(maxx-minx),int(maxy-miny)
  
        coeffs = find_coeffs(
            [(tl[0]-minx,tl[1]-miny), (tr[0]-minx,tr[1]-miny), (dr[0]-minx,dr[1]-miny), (dl[0]-minx,dl[1]-miny)],
            [(0, 0), (img.width, 0), (img.width, img.height), (0, img.height)]
        )

        img1 = img.transform((width, height), Surface3d.PERSPECTIVE, coeffs, self.resampling)
        if img1.width == 0 or img1.height == 0:
            return
        screen.blit(pygame.image.fromstring(img1.tobytes(), img1.size, img1.mode), [minx,miny])
