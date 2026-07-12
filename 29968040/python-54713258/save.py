import nbtlib as nbt
import _base36 as base36
import logging
import numpy as np
import chunk

all_pos = np.array([[[[x, y, z] for z in range(chunk.CHUNK_LENGTH)]
                    for y in range(chunk.CHUNK_HEIGHT)]
                    for x in range(chunk.CHUNK_WIDTH)], dtype=np.uint8)


class Save:
    def __init__(self, world, path="save"):
        self.world = world
        self.path = path
    
    def chunk_position_to_path(self, chunk_position):
        x, _, z = chunk_position

        chunk_path = '/'.join((self.path,
                               base36.dumps(x % 64), base36.dumps(z % 64),
                               f"c.{base36.dumps(x)}.{base36.dumps(z)}.dat"))
        
        return chunk_path

    def load_chunk(self, chunk_position):
        logging.debug(f"Loading chunk at position {chunk_position}")
        # load the chunk file
        
        chunk_path = self.chunk_position_to_path(chunk_position)

        try:
            chunk_blocks = np.array(nbt.load(chunk_path)['']["Level"]["Blocks"], dtype=np.uint32)
        
        except FileNotFoundError:
            return

        # create chunk and fill it with the blocks from our chunk file

        _chunk = chunk.Chunk(self.world, np.array(chunk_position, dtype=np.int32), init_blocks=False)
        self.world.chunks[chunk_position] = _chunk

        temp_chunk = np.zeros((chunk.CHUNK_WIDTH, chunk.CHUNK_HEIGHT, chunk.CHUNK_LENGTH), dtype=np.uint32)
        for x in range(chunk.CHUNK_WIDTH):
            for z in range(chunk.CHUNK_LENGTH):
                index = x * chunk.CHUNK_LENGTH * chunk.CHUNK_HEIGHT + z * chunk.CHUNK_HEIGHT
                temp_chunk[x, :chunk.CHUNK_HEIGHT, z] = chunk_blocks[index:index + chunk.CHUNK_HEIGHT]
        mask = (temp_chunk == 8) | (temp_chunk == 9) | (temp_chunk == 10) | (temp_chunk == 11)
        temp_chunk[mask] = 0
        _chunk.blocks = temp_chunk.tolist()

        mask = (temp_chunk == self.world.light_blocks[0])
        for number in self.world.light_blocks[1:]:
            mask |= (temp_chunk == number)
        for x, y, z in all_pos[mask]:
            world_pos = (_chunk.position[0] + x, _chunk.position[1] + y, _chunk.position[2] + z)
            self.world.increase_light(world_pos, 15, False)

    def save_chunk(self, chunk_position):
        logging.debug(f"Saving chunk at position {chunk_position}")
        x, y, z = chunk_position
        
        # try to load the chunk file
        # if it doesn't exist, create a new one

        chunk_path = self.chunk_position_to_path(chunk_position)

        try:
            chunk_data = nbt.load(chunk_path)
        
        except FileNotFoundError:
            chunk_data = nbt.File({"": nbt.Compound({"Level": nbt.Compound()})})
            
            chunk_data[""]["Level"]["xPos"] = x
            chunk_data[""]["Level"]["zPos"] = z

        # fill the chunk file with the blocks from our chunk

        chunk_blocks = nbt.ByteArray([0] * (chunk.CHUNK_WIDTH * chunk.CHUNK_HEIGHT * chunk.CHUNK_LENGTH))

        for x in range(chunk.CHUNK_WIDTH):
            for y in range(chunk.CHUNK_HEIGHT):
                for z in range(chunk.CHUNK_LENGTH):
                    chunk_blocks[
                        x * chunk.CHUNK_LENGTH * chunk.CHUNK_HEIGHT +
                        z * chunk.CHUNK_HEIGHT +
                        y] = self.world.chunks[chunk_position].blocks[x][y][z]
        
        # save the chunk file

        chunk_data[""]["Level"]["Blocks"] = chunk_blocks
        chunk_data.save(chunk_path, gzipped=True)

    def load(self):
        logging.info("Loading world")

        # for x in range(-1, 15):
        #     for y in range(-15, 1):
        #         self.load_chunk((x, 0, y))
        if 1 or 0:
            for x in range(-4, 4):
                for y in range(-4, 4):
                    self.load_chunk((x, 0, y))
        else:
            for x in range(-1, 1):
                for y in range(-1, 1):
                    self.load_chunk((x, 0, y))

    def save(self):
        logging.info("Saving world")
        for chunk_position in self.world.chunks:
            if chunk_position[1] != 0:  # reject all chunks above and below the world limit
                continue
        
            _chunk = self.world.chunks[chunk_position]

            if _chunk.modified:
                self.save_chunk(chunk_position)
                _chunk.modified = False
