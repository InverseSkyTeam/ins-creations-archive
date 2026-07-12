from .Block import Block

class DirtTile(Block):
    def __init__(self, _id: int, tex: int):
        super().__init__(_id, tex)
