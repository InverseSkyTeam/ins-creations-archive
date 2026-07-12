import pygame
from pg_event import PgEvent


class Keyboard:
    KEY_SPACE = pygame.K_SPACE
    KEY_LMETA = pygame.K_LMETA
    KEY_UP = pygame.K_UP
    KEY_DOWN = pygame.K_DOWN
    KEY_LEFT = pygame.K_LEFT
    KEY_RIGHT = pygame.K_RIGHT
    KEY_W = pygame.K_w
    KEY_A = pygame.K_a
    KEY_S = pygame.K_s
    KEY_D = pygame.K_d
    KEY_R = pygame.K_r
    KEY_ESCAPE = pygame.K_ESCAPE
    KEY_RETURN = pygame.K_RETURN
    KEY_G = pygame.K_g
    KEY_1 = pygame.K_1
    KEY_2 = pygame.K_2
    KEY_3 = pygame.K_3
    KEY_4 = pygame.K_4
    KEY_6 = pygame.K_6

    _index = -1
    
    @staticmethod
    def create():
        pygame.key.stop_text_input()
    
    @staticmethod
    def isKeyDown(key):
        return pygame.key.get_pressed()[key]
    
    @staticmethod
    def destroy():
        pass

    @staticmethod
    def getEventKeyState():
        return len(PgEvent.key_events) > 0

    @staticmethod
    def next():
        if PgEvent._key_update:
            Keyboard._index = 0
            PgEvent._key_update = False
        else:
            Keyboard._index += 1
        if Keyboard._index >= len(PgEvent.key_events):
            return False
        return True

    @staticmethod
    def getEventKey():
        return PgEvent.key_events[Keyboard._index]
