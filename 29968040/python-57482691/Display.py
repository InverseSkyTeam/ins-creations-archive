import pygame
from pg_event import PgEvent


class Display:
    mode = None
    screen = None
    
    @staticmethod
    def setDisplayMode(mode):
        Display.mode = mode
        
    @staticmethod
    def create():
        pygame.init()
        Display.screen = pygame.display.set_mode(Display.mode.get_size(), pygame.DOUBLEBUF | pygame.OPENGL)
    
    @staticmethod
    def getDisplayMode():
        return Display.mode
    
    @staticmethod
    def destroy():
        pygame.quit()
    
    @staticmethod
    def isCloseRequested():
        PgEvent.update()
        return PgEvent._isCloseRequested

    @staticmethod
    def update():
        pygame.display.flip()
