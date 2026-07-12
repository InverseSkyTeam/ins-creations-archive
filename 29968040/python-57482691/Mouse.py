import pygame
from pg_event import PgEvent


class Mouse:
    @staticmethod
    def create():
        pass
    
    @staticmethod
    def setGrabbed(exclusive):
        pygame.event.set_grab(exclusive)
        pygame.mouse.set_visible(not exclusive)
    
    @staticmethod
    def destroy():
        pass

    @staticmethod
    def getDX():
        return float(PgEvent.mouse_dx)

    @staticmethod
    def getDY():
        return float(-PgEvent.mouse_dy)
