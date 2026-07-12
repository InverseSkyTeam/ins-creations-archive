from .Entity import Entity
from Keyboard import Keyboard

class Player(Entity):
    def __init__(self, world):
        super().__init__(world)
        self.heightOffset = 1.62

    def tick(self):
        self.xo = self.x
        self.yo = self.y
        self.zo = self.z
        xa: float = 0.0
        za: float = 0.0

        if Keyboard.isKeyDown(Keyboard.KEY_R):
            self.resetPos()
        if Keyboard.isKeyDown(Keyboard.KEY_UP) or Keyboard.isKeyDown(Keyboard.KEY_W):
            za -= 1.0
        if Keyboard.isKeyDown(Keyboard.KEY_DOWN) or Keyboard.isKeyDown(Keyboard.KEY_S):
            za += 1.0
        if Keyboard.isKeyDown(Keyboard.KEY_LEFT) or Keyboard.isKeyDown(Keyboard.KEY_A):
            xa -= 1.0
        if Keyboard.isKeyDown(Keyboard.KEY_RIGHT) or Keyboard.isKeyDown(Keyboard.KEY_D):
            xa += 1.0
        if Keyboard.isKeyDown(Keyboard.KEY_SPACE) or Keyboard.isKeyDown(Keyboard.KEY_LMETA):
            if self.onGround:
                self.yd = 0.5

        self.moveRelative(xa, za, 0.1 if self.onGround else 0.05)

        self.yd = self.yd - 0.08
        self.move(self.xd, self.yd, self.zd)
        self.xd *= 0.91
        self.yd *= 0.98
        self.zd *= 0.91

        if self.onGround:
            self.xd *= 0.7
            self.zd *= 0.7
