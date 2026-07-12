import zipfile, sys
with zipfile.ZipFile('./textures.zip', 'r') as zip_ref:
    zip_ref.extractall('.')


def get_py_path():
    return sys.executable


def install_library():
    try:
        import numba
    except ImportError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        try:
            subprocess.check_call([get_py_path(), '-m', 'pip', 'install', "numba==0.56.4"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)


install_library()



import pygame
import player
import texture_manager
import world
import options
import keyboard_mouse
from collections import deque
import sys
import time
import platform
from mod import light_contrast


class InternalConfig:
    def __init__(self, _options):
        self.RENDER_DISTANCE = _options.RENDER_DISTANCE
        self.FOV = _options.FOV
        self.CHUNK_UPDATES = _options.CHUNK_UPDATES
        self.SMOOTH_LIGHTING = _options.SMOOTH_LIGHTING


class Window:
    def __init__(self, w, h):
        self.width, self.height = w, h

        # Options
        self.options = InternalConfig(options)

        # F3 Debug Screen

        self.show_f3 = True

        self.texture_manager = texture_manager.TextureManager(16, 16, 256)

        # create world

        self.world = world.World(None, self.texture_manager, self.options)

        # player stuff

        self.player = player.Player(self.world, self.width, self.height)
        self.world.player = self.player

        self.mouse_captured = False

        # misc stuff

        self.holding = 50

        # controls stuff
        self.controls = [0, 0, 0]

        # mouse and keyboard stuff
        self.keyboard_mouse = keyboard_mouse.Keyboard_Mouse(self)

        # GPU command syncs
        self.fences = deque()

        self.exclusive = False  # 是否隐藏鼠标

        self.system_info = f"""Python: {platform.python_implementation()} {platform.python_version()}
System: {platform.machine()} {platform.system()} {platform.release()} {platform.version()}
CPU: {platform.processor()}
Display: {self.width}x{self.height}"""

        self.f3_text = ''
        self.show_f3 = False

    def update_f3(self, delta_time):
        """Update the F3 debug screen content"""

        player_chunk_pos = world.get_chunk_position(self.player.position)
        player_local_pos = world.get_local_position(self.player.position)
        chunk_count = len(self.world.chunks)
        visible_chunk_count = len(self.world.visible_chunks)
        vertices_count = 0
        indices_count = 0
        visible_vertices_count = 0
        visible_indices_count = 0
        for chunk in self.world.chunks.values():
            if chunk.model.vertices is not None:
                vertices_count += len(chunk.model.vertices)
            if chunk.model.indices is not None:
                indices_count += len(chunk.model.indices)
        for chunk in self.world.visible_chunks:
            if chunk.model.vertices is not None:
                visible_vertices_count += len(chunk.model.vertices)
            if chunk.model.indices is not None:
                visible_indices_count += len(chunk.model.indices)

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

    def on_draw(self, _screen, mod_line_x):
        self.player.update_matrices()

        self.world.prepare_rendering()
        self.world.draw(_screen, mod_line_x)
        if self.show_f3:
            y = 0
            font_size = int(min(self.width, self.height)/30)
            line_height = int(font_size * 1.2)
            font = pygame.font.SysFont('SimHei', font_size)
            for line in self.f3_text.split('\n'):
                _screen.blit(font.render(line, True, (255,)*3), (0, y + (line_height-font_size)//2))
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


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((852, 480), pygame.RESIZABLE)
    window = Window(852, 480)
    clock = pygame.time.Clock()
    pygame.key.stop_text_input()
    last_time = time.time()
    cross_hair = pygame.image.load('crosshair.png').convert_alpha()
    mod_light_contrast = light_contrast.Mod(screen, 0.5)
    use_mod = False
    while True:
        FPS = str(round(clock.get_fps()))
        pygame.display.set_caption('fps:' + FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                window.on_resize(screen.get_width(), screen.get_height())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if use_mod and not window.exclusive and mod_light_contrast.on_mouse_down(event.pos):
                    continue
                window.on_mouse_press(event.button)
            elif event.type == pygame.MOUSEMOTION:
                if use_mod and not window.exclusive and mod_light_contrast.on_mouse_motion(event.rel[0]):
                    continue
                window.on_mouse_motion(*event.rel)
            elif event.type == pygame.MOUSEBUTTONUP:
                if use_mod:
                    mod_light_contrast.on_mouse_up()
            elif event.type == pygame.KEYDOWN:
                window.on_key_press(event.key)
                if event.key == pygame.K_l:
                    use_mod = not use_mod
                    mod_light_contrast.dragging = False
            elif event.type == pygame.KEYUP:
                window.on_key_release(event.key)
        screen.fill((255, 255, 255))

        window.player.update_interpolation(delta_time=time.time()-last_time)
        window.update(delta_time=time.time()-last_time)
        last_time = time.time()

        window.on_draw(screen, mod_light_contrast.line_x if use_mod else None)
        screen.blit(cross_hair, cross_hair.get_rect(center=screen.get_rect().center))
        if use_mod:
            mod_light_contrast.draw()

        pygame.display.update()
        clock.tick(114514)
