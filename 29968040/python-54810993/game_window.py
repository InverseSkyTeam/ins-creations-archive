import player
import texture_manager
import world
import keyboard_mouse
import platform
import pygame
from font_manager import FontManager


class Window:
    def __init__(self, w, h, options):
        self.width, self.height = w, h

        # Options
        self.options = options

        # F3 Debug Screen

        self.show_f3 = True

        self.texture_manager = texture_manager.TextureManager(16, 16, 256)

        # create world

        self.world = world.World(None, self.texture_manager, self.options)

        # player stuff

        self.player = player.Player(self.world, self.width, self.height)
        self.world.player = self.player

        self.mouse_captured = False

        self.holding = 50  # 手持方块的编号

        # controls stuff
        self.controls = [0, 0, 0]

        # mouse and keyboard stuff
        self.keyboard_mouse = keyboard_mouse.Keyboard_Mouse(self)

        self.exclusive = False  # 是否隐藏鼠标

        self.system_info = f"""Python: {platform.python_implementation()} {platform.python_version()}
System: {platform.machine()} {platform.system()} {platform.release()} {platform.version()}
CPU: {platform.processor()}
Display: {self.width}x{self.height}"""

        self.f3_text = ''
        self.show_f3 = False
        self.font_manager = FontManager()

    def update_f3(self, delta_time):
        """Update the F3 debug screen content"""

        player_chunk_pos = world.get_chunk_position(self.player.position)
        player_local_pos = world.get_local_position(self.player.position)
        chunk_count = len(self.world.chunks)
        visible_chunk_count = len(self.world.visible_chunks)
        vertices_count = sum(
            len(chunk.model.vertices) for chunk in self.world.chunks.values() if chunk.model.vertices is not None)
        indices_count = sum(
            len(chunk.model.indices) for chunk in self.world.chunks.values() if chunk.model.indices is not None)
        visible_vertices_count = sum(
            len(chunk.model.vertices) for chunk in self.world.visible_chunks if chunk.model.vertices is not None)
        visible_indices_count = sum(
            len(chunk.model.indices) for chunk in self.world.visible_chunks if chunk.model.indices is not None)
        self.f3_text = \
            f"""IDU-3D沙盒 v0.1.1
{round(1 / delta_time)} FPS ({self.world.chunk_update_counter} Chunk Updates)
C: {visible_chunk_count}/{chunk_count} pC: {self.world.pending_chunk_update_count} pU: {len(self.world.chunk_building_queue)} aB: {chunk_count}

XYZ: {round(self.player.position[0], 3)} / {round(self.player.position[1], 3)} / {round(self.player.position[2], 3)}
Block: {self.player.rounded_position[0]} {self.player.rounded_position[1]} {self.player.rounded_position[2]}
Chunk: {player_local_pos[0]} {player_local_pos[1]} {player_local_pos[2]} in {player_chunk_pos[0]} {player_chunk_pos[1]} {player_chunk_pos[2]}
Client Light: {max(self.world.get_light(self.player.rounded_position), self.world.get_skylight(self.player.rounded_position))} ({self.world.get_skylight(self.player.rounded_position)} sky, {self.world.get_light(self.player.rounded_position)} block)

{self.system_info}

Renderer: {"INS-Sandbox3D v0.0.1"}
Data: {vertices_count}个顶点, {indices_count}个面
Visible Data: {visible_vertices_count}个顶点, {visible_indices_count}个面
"""

    def set_exclusive_mouse(self, exclusive):  # 设置鼠标是否隐藏
        pygame.event.set_grab(exclusive)
        pygame.mouse.set_visible(not exclusive)
        self.exclusive = exclusive

    def update(self, delta_time):
        """Every tick"""
        if self.show_f3:
            self.update_f3(delta_time)
        if not self.mouse_captured:
            self.player.input = [0, 0, 0]

        self.player.update(delta_time)
        self.world.tick(delta_time)

    def on_draw(self, _screen):
        self.player.update_matrices()

        self.world.prepare_rendering()
        self.world.draw(_screen)

    def render_f3(self, screen):
        if self.show_f3:
            y = 0
            font_size = int(min(screen.get_size()) / 30)
            line_height = int(font_size * 1.2)
            font = self.font_manager.SysFont('SimHei', font_size)
            for line in self.f3_text.split('\n'):
                screen.blit(font.render(line, True, (255,) * 3), (0, y + (line_height - font_size) // 2))
                y += line_height

    def on_resize(self, width, height):
        self.player.view_width = width
        self.player.view_height = height
        self.width, self.height = width, height

    def on_mouse_press(self, button):
        pass

    def on_mouse_motion(self, delta_x, delta_y):
        pass

    def on_key_press(self, key):
        pass

    def on_key_release(self, key):
        pass
