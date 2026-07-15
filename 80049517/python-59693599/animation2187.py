import pygame
from typing import Tuple


class _AnimationWrapper(object):
    def __init__(self, func: "function"):
        self._args = []
        self._kwargs = {}
        self.done = True

        self.func = func

    def __call__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self.done = False
    
    def call(self):
        if len(self._args) == 0 and len(self._kwargs) == 0:
            return
        self.func(*self._args, **self._kwargs)


class Animation2187(object):
    def __init__(self, sprite: pygame.sprite.Sprite):
        self.sprite = sprite

        self.move = _AnimationWrapper(self._move)

    def _move(self, pos: Tuple[int, int], speed: float):
        if speed >= 1:
            raise ValueError
        
        if (
            abs(self.sprite.rect.x - pos[0]) < 1
            and abs(self.sprite.rect.y - pos[1]) < 1
        ):
            self.sprite.rect.x = pos[0]
            self.sprite.rect.y = pos[1]
            self.move.done = True
        else:
            self.sprite.rect.x += (pos[0] - self.sprite.rect.x) * speed
            self.sprite.rect.y += (pos[1] - self.sprite.rect.y) * speed

    def update(self):
        self.move.call()
