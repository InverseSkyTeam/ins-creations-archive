# 正在制作中

import numpy as np
from world import sectorize
import time

from configure import *
from render import NoneModel


class WorldDrops:
    def __init__(self):
        self.world_drops = {}
        self.sectors_drops = {}
        self._shown_drops_vertices = {}
        self._shown_drops_indices = {}
        self._shown_drops_uv_indices = {}
        self.model_drop = NoneModel(all_textures.texture_array, None, all_textures.uv_vertices, None, None, None,
                                    all_textures.texture_width, all_textures.texture_height)

    def add_drop(self, texture, position):
        self.world_drops[position] = texture.drop
        self.sectors_drops.setdefault(sectorize(position), []).append(position)
        self._show_drop(position, texture.drop)

    def remove_drop(self, position):
        del self.world_drops[position]
        self.sectors_drops[sectorize(position)].remove(position)
        self._hide_drop(position)

    def _hide_drop(self, position):
        self._shown_drops_vertices.pop(position)
        self._shown_drops_indices.pop(position)
        self._shown_drops_uv_indices.pop(position)

    def _show_drop(self, position, texture):
        x, y, z = position
        new_vertices = texture.vertices.copy()
        new_vertices[:, 0, 0] += x
        new_vertices[:, 1, 0] += y
        new_vertices[:, 2, 0] += z
        self._shown_drops_vertices[position] = new_vertices
        self._shown_drops_indices[position] = texture.indices.copy()
        self._shown_drops_uv_indices[position] = texture.uv_indices.copy()

    def show_sector(self, sector):
        """确保需要显示的给定区块中的所有方块都绘制到画布上。

        """
        for position in self.sectors_drops.get(sector, []):
            if position not in self._shown_drops_indices:
                self._show_drop(position, self.world_drops[position])

    def hide_sector(self, sector):
        """确保需要隐藏的给定区块中的所有方块都从画布中移除。

        """
        for position in self.sectors_drops.get(sector, []):
            if position in self._shown_drops_indices:
                self._hide_drop(position)

    def render_drop(self):
        cube_num = len(self._shown_drops_vertices)
        if cube_num == 0:
            return True
        vertices = np.concatenate(list(self._shown_drops_vertices.values()), axis=0)
        vertices_add = np.concatenate(list(self._shown_drops_vertices.keys()), axis=0)
        addx, addz = vertices_add[np.arange(0, cube_num*3, 3)], vertices_add[np.arange(2, cube_num*3, 3)]
        addx = np.repeat(addx, 8)
        addz = np.repeat(addz, 8)
        indices = np.concatenate(list(self._shown_drops_indices.values()), axis=0)
        uv_indices = np.concatenate(list(self._shown_drops_uv_indices.values()), axis=0)
        indices += np.repeat(np.arange(0, cube_num * 8, 8), repeats=12)[:, None]
        vertices[:, 1, 0] += 0.05 * math.sin(time.time())
        vertices[:, 0, 0] -= addx
        vertices[:, 2, 0] -= addz
        angle = time.time()
        vertices[:, 0, 0], vertices[:, 2, 0] = vertices[:, 2, 0] * np.sin(angle) + vertices[:, 0, 0] * np.cos(angle), \
                                               vertices[:, 2, 0] * np.cos(angle) - vertices[:, 0, 0] * np.sin(angle)
        vertices[:, 0, 0] += addx
        vertices[:, 2, 0] += addz
        self.model_drop.vertices = vertices
        self.model_drop.indices = indices
        self.model_drop.uv_indices = uv_indices
        self.model_drop.norms = DIRT.norms
        return False
