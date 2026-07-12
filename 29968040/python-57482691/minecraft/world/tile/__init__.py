from .Block import Block
from .DirtTile import DirtTile
from .GrassTile import GrassTile
from .Bush import Bush

Block.rock = Block(1, 1)
Block.grass = GrassTile(2)
Block.dirt = DirtTile(3, 2)
Block.stoneBrick = Block(4, 16)
Block.wood = Block(5, 4)
Block.bush = Bush(6)
