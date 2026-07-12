from render import Render
from control import Control
from people_manager import PeopleManager


class Window:
    def __init__(self):
        self.people_manager = PeopleManager()
        self.control = Control(self.people_manager)
        self.render = Render(self.people_manager)
        self.people_manager.control = self.control
        self.people_manager.init()

    def draw(self, screen, w, h):
        screen.fill((0,) * 3)
        self.render.render3d(screen, w, h, self.control.angle_alpha, self.control.angle_beta,
                             self.control.tx, self.control.ty, self.control.tz)
        self.render.render2d(screen, w, h, self.control.is_attack)

        # self.control.ray.debug_ray(screen, self.control.tx, self.control.ty, self.control.tz,
        #                            self.people_manager.peoples)

    def update(self, events):
        self.control.update(events)
