from PyNa import *
import pygame
import time

pygame.init()


class Counter(NThread):
    update_count: NSignal[int]

    def run(self):
        count = 0
        while True:
            time.sleep(1)
            count += 1
            self.update_count.emit(count)
            print(f"[Counter Thread] Update Count To: {count}")


class Application(NCoreApplication):
    def __init__(self, screen: pygame.surface.Surface):
        super().__init__()
        self.screen = screen
        self.ticks = 60
        self.running = False

        self.count = 0
        self.counter = Counter()
        self.counter.update_count.connect(lambda count: setattr(self, "count", count))

    def process_event(self, events: list[NEvent]):
        for event in events:
            if event.name == "pygame_event":
                pg_event: pygame.event.Event = event.arg
                if pg_event.type == pygame.QUIT:
                    self.running = False

    def render(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(font.render(f"Count: {self.count}", True, (0, 0, 0)), (20, 20))


screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 48)
clock = pygame.time.Clock()
app = Application(screen)

app.running = True
app.counter.start()
while app.running:
    for event in pygame.event.get():
        app.push_event(NEvent("pygame_event", event))
    app.process_event(app.get_events())
    app.render()

    pygame.display.update()
    clock.tick(app.ticks)

pygame.quit()
app.counter.stop()
