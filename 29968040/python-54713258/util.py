import numpy as np
import pygame.math


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

chunk1 = pygame.math.Vector3(CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2)
chunk2 = pygame.math.Vector3(CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2)
chunk3 = pygame.math.Vector3(-CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2)
chunk4 = pygame.math.Vector3(CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2)
chunk5 = pygame.math.Vector3(-CHUNK_WIDTH / 2, CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2)
chunk6 = pygame.math.Vector3(CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2)
chunk7 = pygame.math.Vector3(-CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, CHUNK_LENGTH / 2)
chunk8 = pygame.math.Vector3(CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2)
chunk9 = pygame.math.Vector3(-CHUNK_WIDTH / 2, -CHUNK_HEIGHT / 2, -CHUNK_LENGTH / 2)
