import numpy as np
from util import CHUNK_WIDTH, CHUNK_LENGTH, CHUNK_HEIGHT
from numba import njit


chunk0 = np.array([CHUNK_WIDTH, 0, CHUNK_LENGTH], dtype=np.int32)
chunk1 = np.array([CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2], dtype=np.int32)
chunk2 = np.array([CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2], dtype=np.float64)
chunk3 = np.array([-CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2], dtype=np.float64)
chunk4 = np.array([CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2], dtype=np.float64)
chunk5 = np.array([-CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2], dtype=np.float64)
chunk6 = np.array([CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2], dtype=np.float64)
chunk7 = np.array([-CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2], dtype=np.float64)
chunk8 = np.array([CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2], dtype=np.float64)
chunk9 = np.array([-CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2], dtype=np.float64)


@njit(fastmath=True)
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


@njit(looplift=True, fastmath=True)
def check_in_frustum(chunk_pos, planes):
    """Frustum check of each chunk. If the chunk is not in the view frustum, it is discarded"""
    result = 2
    center = (chunk_pos * chunk0 + chunk1).astype(np.float64)

    for plane in planes:
        _in = 0
        _out = 0
        normal = plane[:3]
        w = plane[3]
        if dot(normal, center + chunk2) + w < 0:
            _out += 1
        else:
            _in += 1
        if dot(normal, center + chunk3) + w < 0:
            _out += 1
        else:
            _in += 1
        if dot(normal, center + chunk4) + w < 0:
            _out += 1
        else:
            _in += 1
        if dot(normal, center + chunk5) + w < 0:
            _out += 1
        else:
            _in += 1
        if dot(normal, center + chunk6) + w < 0:
            _out += 1
        else:
            _in += 1
        if dot(normal, center + chunk7) + w < 0:
            _out += 1
        else:
            _in += 1
        if dot(normal, center + chunk8) + w < 0:
            _out += 1
        else:
            _in += 1
        if dot(normal, center + chunk9) + w < 0:
            _out += 1
        else:
            _in += 1

        if not _in:
            return 0
        elif _out:
            result = 1
    return result
