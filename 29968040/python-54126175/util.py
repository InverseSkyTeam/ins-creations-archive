import numpy as np


DIRECTIONS_TUPLE = ((1, 0, 0),
                    (-1, 0, 0),
                    (0, 1, 0),
                    (0, -1, 0),
                    (0, 0, 1),
                    (0, 0, -1))

EAST = np.array([1, 0, 0], dtype=np.int32)
WEST = np.array([-1, 0, 0], dtype=np.int32)
UP = np.array([0, 1, 0], dtype=np.int32)
DOWN = np.array([0, -1, 0], dtype=np.int32)
SOUTH = np.array([0, 0, 1], dtype=np.int32)
NORTH = np.array([0, 0, -1], dtype=np.int32)

UP_SOUTH = tuple(UP + SOUTH)
UP_NORTH = tuple(UP + NORTH)
UP_EAST = tuple(UP + EAST)
UP_WEST = tuple(UP + WEST)
DOWN_SOUTH = tuple(DOWN + SOUTH)
DOWN_NORTH = tuple(DOWN + NORTH)
DOWN_EAST = tuple(DOWN + EAST)
DOWN_WEST = tuple(DOWN + WEST)
SOUTH_EAST = tuple(SOUTH + EAST)
SOUTH_WEST = tuple(SOUTH + WEST)
NORTH_EAST = tuple(NORTH + EAST)
NORTH_WEST = tuple(NORTH + WEST)
EAST = tuple(EAST)
WEST = tuple(WEST)
UP = tuple(UP)
DOWN = tuple(DOWN)
NORTH = tuple(NORTH)
SOUTH = tuple(SOUTH)

CHUNK_WIDTH = 16  # 区块宽
CHUNK_HEIGHT = 128  # 区块高
CHUNK_LENGTH = 16  # 区块长

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
