from render import Render
from control import Control
from people_manager import PeopleManager
from message import Message
from skill import SharpnessSkill, SwiftnessSkill


class Window:
    def __init__(self, w, h, project):
        self.message = Message()
        self.people_manager = PeopleManager(self.message, project)
        self.control = Control(self.people_manager)
        self.render = Render(self.people_manager, self.control)
        self.skills = [SharpnessSkill(self.control, w, h), SwiftnessSkill(self.control, w, h)]
        self.people_manager.control = self.control
        self.people_manager.init()

    def draw(self, screen, w, h):
        screen.fill((0,) * 3)
        self.render.render3d(screen, w, h)
        self.render.render2d(screen, w, h)
        for skill in self.skills:
            skill.render(screen)
        self.render.render_ui(screen, w, h)

        self.message.render(screen)

        # self.control.ray.debug_ray(screen, self.control.tx, self.control.ty, self.control.tz,
        #                            self.people_manager.peoples)

    def update(self, events):
        self.control.update(events, self.skills)
        for skill in self.skills:
            skill.update()

    def exit(self):
        self.people_manager.exit = True
        self.control.set_exclusive_mouse(False)
