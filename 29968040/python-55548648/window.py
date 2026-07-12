from render import Render
from control import Control


class Window:
    def __init__(self):
        self.control = Control()
        self.render = Render()

    def draw(self, screen, w, h):
        screen.fill((0,) * 3)
        self.render.render3d(screen, w, h, self.control.angle_alpha, self.control.angle_beta,
                             self.control.tx, self.control.ty, self.control.tz)

    def update(self, events):
        self.control.update(events)
