from config import Config
from util import clamp, clampLng, ease_in_out_cubic
import pygame
from enum import IntEnum
import time
from control_ui import UI
import math


class FocusType(IntEnum):
    NONE = 0
    DRAG_GLOBE = 1
    DRAG_UI = 2


class Control:
    def __init__(self):
        self.mouse_focus = FocusType.NONE
        self.in_animation = False
        self.prev_time = time.time()
        self.ui = UI(self.go_to)

        self.drag_x = None
        self.drag_y = None
        self.drag_lat = None
        self.drag_lng = None

        self.anim_start = None
        self.anim_middle = None
        self.anim_end = None

        self.anim_start_lat = None
        self.anim_start_lng = None
        self.anim_start_zoom = None
        self.anim_end_lat = None
        self.anim_end_lng = None
        self.anim_end_zoom = None

    def on_mouse_down(self, event, w):
        if (event.button == 1 or event.button == 3) and not self.in_animation:
            if self.ui.collide_left(w, event.pos):
                self.mouse_focus = FocusType.DRAG_UI
                return
            if self.ui.colide_ui(w, event.pos):
                self.ui.handle_mouse_down(w, event.pos)
                return
            self.mouse_focus = FocusType.DRAG_GLOBE
            self.drag_x, self.drag_y = event.pos
            self.drag_lat = Config.lat
            self.drag_lng = Config.lng

    def on_mouse_motion(self, event):
        if self.mouse_focus == FocusType.DRAG_GLOBE:
            dx = event.pos[0] - self.drag_x
            dy = event.pos[1] - self.drag_y
            Config.lat = clamp(self.drag_lat + dy * 0.5, -90, 90)
            Config.lng = clampLng(self.drag_lng - dx * 0.5)
        elif self.mouse_focus == FocusType.DRAG_UI:
            self.ui.width -= event.rel[0]
            self.ui.width = max(self.ui.width, 20)

    def on_mouse_up(self, event, w):
        if event.button == 1 or event.button == 3:
            if self.mouse_focus == FocusType.NONE and not self.ui.open and self.ui.colide_ui(w, event.pos):
                self.ui.open = not self.ui.open
            self.mouse_focus = FocusType.NONE

    def handle_event(self, events, w):
        if self.mouse_focus == FocusType.NONE and pygame.mouse.get_pressed()[0] and \
                self.ui.open and not self.in_animation:
            self.ui.handle_mouse(w, pygame.mouse.get_pos())
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.on_mouse_down(event, w)
            if event.type == pygame.MOUSEMOTION:
                self.on_mouse_motion(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.on_mouse_up(event, w)

    def render(self, screen, w):
        self.ui.render(screen, w)

    def update(self):
        curv_time = time.time()
        time_step = curv_time - self.prev_time
        self.prev_time = curv_time

        if Config.autoSpin and self.mouse_focus != FocusType.DRAG_GLOBE and not self.in_animation:
            Config.lng = clampLng(Config.lng - 0.2 * 60 * time_step)

        if self.in_animation:
            if self.anim_start <= curv_time <= self.anim_middle:
                t = ease_in_out_cubic((curv_time - self.anim_start)/(self.anim_middle - self.anim_start))
                Config.lat = self.anim_start_lat + (self.anim_end_lat - self.anim_start_lat) * t
                Config.lng = self.anim_start_lng + (self.anim_end_lng - self.anim_start_lng) * t
            elif self.anim_middle < curv_time <= self.anim_end:
                Config.lat, Config.lng = self.anim_end_lat, self.anim_end_lng
                t = ease_in_out_cubic((curv_time - self.anim_middle) / (self.anim_end - self.anim_middle))
                Config.zoom = self.anim_start_zoom + (self.anim_end_zoom - self.anim_start_zoom) * t
            else:
                self.in_animation = False
                Config.lat, Config.lng, Config.zoom = self.anim_end_lat, self.anim_end_lng, self.anim_end_zoom
                return

    def go_to(self, lat, lng):
        d_x = lat - Config.lat
        d_y = lng - Config.lng
        rough_distance = math.sqrt(d_x * d_x + d_y * d_y)

        self.anim_start_lat = Config.lat
        self.anim_start_lng = Config.lng
        self.anim_start_zoom = Config.zoom
        self.anim_end_lat = lat
        self.anim_end_lng = lng
        self.anim_end_zoom = 1

        self.anim_start = time.time()
        self.anim_middle = self.anim_start + rough_distance * 0.01
        self.anim_end = self.anim_middle + 1
        self.in_animation = True
