import numpy as np
import pygame

from matrix import update_matrix
from world import World
from cancel_text import CancelText
from inventory import Inventory, BackPack
from player import Player
from block_data import AllBlockData, cube_model
from render import render_cube, ModelOld, WorldModel
from configure import DIRT


model_old = ModelOld('data/models/2d_screen.obj', div_num=(5, 3.5), pos=(30, 26, 81))


class Window:
    def __init__(self, screen):
        self.exclusive = False  # 是否隐藏鼠标

        self.screen = screen

        self.interface = 'main'  # 当前界面 main: 主界面， backpack: 背包界面

        self.cancel_text = CancelText()

        # 处理世界的模型实例。
        self.block_data = AllBlockData()
        self.world = World(self.block_data)
        self.inventory = Inventory(screen, self.block_data)
        self.backpack = BackPack(screen, self.inventory, self.block_data)
        self.player = Player(self.world, self.inventory, self.block_data)

    def compile_aot(self):
        tmp_model = WorldModel(self.block_data.texture_manager, cube_model.uv_vertices, cube_model.uv_indices)
        tmp_model.vertices = cube_model.vertices
        tmp_model.indices = cube_model.indices
        tmp_model.uv_index = self.block_data[DIRT].tex_indices_triangle
        z_buffer = np.full((10, 10), np.inf, dtype=np.float64)  # 深度缓冲数组
        temp_matrix = update_matrix((0, 0, 0), (0, 0, 0), False, 0, 10, 10)
        render_cube(tmp_model, pygame.Surface((10, 10)), z_buffer, temp_matrix)

    def initialize(self, seed):
        self.world.initialize(seed)  # 生成世界

    def set_exclusive_mouse(self, exclusive):  # 设置鼠标是否隐藏
        pygame.event.set_grab(exclusive)
        pygame.mouse.set_visible(not exclusive)
        self.exclusive = exclusive

    def handle_event(self, events, mouse_pos_screen):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.inventory.inventory_index -= 1
                    self.inventory.inventory_index %= 9
                    continue
                if event.button == 5:
                    self.inventory.inventory_index += 1
                    self.inventory.inventory_index %= 9
                    continue
                self.on_mouse_press(event.button, event.pos, mouse_pos_screen)
            elif event.type == pygame.MOUSEMOTION:
                self.on_mouse_motion(*event.rel)
            elif event.type == pygame.KEYDOWN:
                self.on_key_press(event.key)
            elif event.type == pygame.KEYUP:
                self.on_key_release(event.key)
            elif event.type == pygame.VIDEORESIZE:
                self.backpack.update_size()
                self.inventory.update_size()

    def on_mouse_press(self, button, pos, mouse_pos_screen):
        """ 当鼠标按下时调用。"""
        if self.interface == 'backpack':
            self.backpack.on_mouse_press(button, pos)
            return
        is_screen = 0 <= mouse_pos_screen[0] < 1000 and 0 <= mouse_pos_screen[1] < 700
        if self.exclusive:
            if is_screen:
                return
            self.player.on_mouse_press(button)
        else:
            self.set_exclusive_mouse(True)
            self.cancel_text.start_anim()

    def on_mouse_motion(self, dx, dy):
        """ 当玩家移动鼠标时调用。

        参数
        ----------
        x, y : int
            鼠标点击的坐标。如果鼠标被捕获，则始终为屏幕中心。
        dx, dy : float
            鼠标的移动距离。

        """
        if self.exclusive and self.interface == 'main':
            self.player.on_mouse_motion(dx, dy)
        if self.interface == 'backpack':
            self.backpack.on_mouse_motion((dx, dy))

    def on_key_press(self, symbol):
        """ 当玩家按下键时调用。请参阅 pyglet 文档以获取键的映射。

        参数
        ----------
        symbol : int
            表示被按下的键的数字。
        """
        if symbol == pygame.K_e:
            self.interface = {'main': 'backpack', 'backpack': 'main'}[self.interface]
            pygame.mouse.set_visible(True if not self.exclusive else self.interface == 'backpack')
            # TODO: 未实现关闭背包时把物品丢出
            self.backpack.focus_texture = self.backpack.focus_num = self.backpack.focus_rect = None
            self.backpack.move = False
        elif symbol == pygame.K_ESCAPE:
            self.set_exclusive_mouse(False)
            self.cancel_text.end_anim()
        else:
            self.player.on_key_press(symbol)

    def on_key_release(self, symbol):
        """当玩家释放一个键时调用。symbol代表按下的键，modifiers代表其他同时按下的修饰键。

        参数
        ----------
        symbol : int
            表示被按下的键的数字
        """
        self.player.on_key_release(symbol)

    def hit_test_screen(self):
        return self.player.hit_test_screen(model_old)

    def update(self):
        self.player.update()

    def render_ui(self, width, height):
        pygame.draw.line(self.screen, (0,) * 3, (width // 2 - 10, height // 2), (width // 2 + 10, height // 2))
        pygame.draw.line(self.screen, (0,) * 3, (width // 2, height // 2 - 10), (width // 2, height // 2 + 10))
        self.inventory.render()
        if self.interface == 'backpack':
            self.backpack.render()
        self.cancel_text.render(self.screen)

    def render_3d(self, width, height, screen1):
        z_buffer = np.full(self.screen.get_size(), np.inf, dtype=np.float64)  # 深度缓冲数组

        final_matrix = update_matrix(self.player.rotation, self.player.position, self.player.crouch, self.player.fov_offset, width, height)
        
        model_old.texture_array[0] = pygame.surfarray.pixels2d(screen1).copy()
        render_cube(model_old, self.screen, z_buffer, final_matrix, False)
        
        res = self.world.render()  # 方块模型
        # res1 = self.world.render_drop()  # 掉落物模型

        if not res:
            render_cube(self.world.model, self.screen, z_buffer, final_matrix)
            focused_model, _ = self.player.get_focused_block()
            if focused_model:
                render_cube(focused_model, self.screen, z_buffer, final_matrix)
            
        # if not res1:
        #     render_cube(self.world.model_drop, self.screen, z_buffer, final_matrix)

    def on_draw(self, screen1):  # 绘制画布
        width, height = self.screen.get_size()
        self.render_3d(width, height, screen1)
        self.render_ui(width, height)
