import time


class DirtyChunkSorter:
    def __init__(self, player, frustum):
        self.player = player
        self.frustum = frustum
        self.now = int(time.time() * 1000)

    def compare(self, c0, c1):
        i0: bool = self.frustum.cubeInFrustum(c0.aabb.x0, c0.aabb.y0, c0.aabb.z0, c0.aabb.x1, c0.aabb.y1, c0.aabb.z1)
        i1: bool = self.frustum.cubeInFrustum(c1.aabb.x0, c1.aabb.y0, c1.aabb.z0, c1.aabb.x1, c1.aabb.y1, c1.aabb.z1)
        if i0 and not i1:
            return -1
        if i1 and not i0:
            return 1
        t0: int = (self.now - c0.dirtiedTime) // 2000
        t1: int = (self.now - c1.dirtiedTime) // 2000
        if t0 < t1:
            return -1
        if t0 > t1:
            return 1
        return -1 if c0.distanceToSqr(self.player) < c1.distanceToSqr(self.player) else 1
