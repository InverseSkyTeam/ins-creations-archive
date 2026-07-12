import pygame


class PgEvent:
    key_events = []
    _key_update = False
    _isCloseRequested = False
    mouse_dx: float = 0.0
    mouse_dy: float = 0.0

    @staticmethod
    def update():
        PgEvent.mouse_dx, PgEvent.mouse_dy = 0.0, 0.0
        PgEvent.key_events = []
        PgEvent._key_update = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PgEvent._isCloseRequested = True
            elif event.type == pygame.MOUSEMOTION:
                PgEvent.mouse_dx, PgEvent.mouse_dy = event.rel
            elif event.type == pygame.KEYDOWN:
                PgEvent.key_events.append(event.key)
