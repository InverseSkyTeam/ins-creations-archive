import pygame

class Core:
    def __init__(self, **api):
        self.alive = True
        self.api = api
        self.operations = {
            pygame.QUIT: self.call_exit,
            pygame.MOUSEBUTTONDOWN: self.call_btn_down,
            'call_click': self.call_click,
        }
    def __getitem__(self, key):
        return self.api[key]
    def __setitem__(self, key, value):
        self.api[key] = value
    
    
    @staticmethod
    def activate(name, **data):
        event = pygame.event.Event(pygame.USEREVENT, name = name, **data)
        pygame.event.post(event)
    
    def handle(self, event):
        exe = self.operations.get(event.name if event.type == pygame.USEREVENT else event.type, None)
        if exe: exe(event)     # exe缩写名词转动词，妙！（
    
    def update(self):
        self['screen'].fill((255, 255, 255))       # screen.fill((255, 255, 255))
        pygame.display.update()
    
    def call_exit(self, event):
        self.alive = False
    def call_btn_down(self, event):
        if event.button == 1:
            self.activate('call_click', target='screen')
    def call_click(self, event):
        if event.target == 'screen':
            print('mouse left clicked on screen!')