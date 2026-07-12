import pygame
import controller
import math


class Keyboard_Mouse(controller.Controller):
    def __init__(self, game):
        super().__init__(game)

        self.game.on_mouse_press = self.on_mouse_press
        self.game.on_mouse_motion = self.on_mouse_motion

        self.game.on_key_press = self.on_key_press
        self.game.on_key_release = self.on_key_release

    def on_mouse_press(self, button):
        if not self.game.mouse_captured:
            self.game.mouse_captured = True
            self.game.set_exclusive_mouse(True)

            return

        if button == 3: self.interact(self.InteractMode.PLACE)
        elif button == 1: self.interact(self.InteractMode.BREAK)
        elif button == 2: self.interact(self.InteractMode.PICK)

    def on_mouse_motion(self, delta_x, delta_y):
        delta_y = -delta_y
        if self.game.mouse_captured:
            sensitivity = 0.004

            self.game.player.rotation[0] += delta_x * sensitivity
            self.game.player.rotation[1] += delta_y * sensitivity

            self.game.player.rotation[1] = max(-math.tau / 4, min(math.tau / 4, self.game.player.rotation[1]))

    def on_key_press(self, key):
        if not self.game.mouse_captured:
            return

        if key == pygame.K_d: self.start_move(self.MoveMode.RIGHT)
        elif key == pygame.K_a: self.start_move(self.MoveMode.LEFT)
        elif key == pygame.K_w: self.start_move(self.MoveMode.FORWARD)
        elif key == pygame.K_s: self.start_move(self.MoveMode.BACKWARD)
        elif key == pygame.K_SPACE : self.start_move(self.MoveMode.UP)
        elif key == pygame.K_LSHIFT: self.start_move(self.MoveMode.DOWN)

        elif key == pygame.K_LCTRL : self.start_modifier(self.ModifierMode.SPRINT)

        elif key == pygame.K_f: self.misc(self.MiscMode.FLY)
        elif key == pygame.K_g: self.misc(self.MiscMode.RANDOM)
        elif key == pygame.K_o: self.misc(self.MiscMode.SAVE)
        elif key == pygame.K_r: self.misc(self.MiscMode.TELEPORT)
        elif key == pygame.K_ESCAPE: self.misc(self.MiscMode.ESCAPE)
        elif key == pygame.K_F6: self.misc(self.MiscMode.SPEED_TIME)
        # elif key == pygame.K_F11: self.misc(self.MiscMode.FULLSCREEN)
        elif key == pygame.K_F3: self.misc(self.MiscMode.TOGGLE_F3)
        elif key == pygame.K_F10: self.misc(self.MiscMode.TOGGLE_AO)

    def on_key_release(self, key):
        if not self.game.mouse_captured:
            return

        if key == pygame.K_d: self.end_move(self.MoveMode.RIGHT)
        elif key == pygame.K_a: self.end_move(self.MoveMode.LEFT)
        elif key == pygame.K_w: self.end_move(self.MoveMode.FORWARD)
        elif key == pygame.K_s: self.end_move(self.MoveMode.BACKWARD)
        elif key == pygame.K_SPACE : self.end_move(self.MoveMode.UP)
        elif key == pygame.K_LSHIFT: self.end_move(self.MoveMode.DOWN)

        elif key == pygame.K_LCTRL : self.end_modifier(self.ModifierMode.SPRINT)
