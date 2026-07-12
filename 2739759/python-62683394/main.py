import pygame
import sys
import math
from pygame.locals import *

# 初始化pygame
pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("物理世界模拟器 - 终极优化版")

# 颜色定义
BACKGROUND = (20, 30, 50)
GRID_COLOR = (40, 60, 80)
OBSTACLE_COLOR = (70, 130, 180)
OBSTACLE_HIGHLIGHT = (100, 180, 255)
BALL_COLOR = (220, 100, 100)
BALL_HIGHLIGHT = (255, 150, 150)
UI_BG = (30, 40, 60, 200)
UI_BORDER = (70, 100, 140)
TEXT_COLOR = (220, 220, 220)
SLIDER_BG = (50, 70, 100)
SLIDER_FG = (100, 180, 255)
MENU_BG = (40, 50, 70, 240)
MENU_HIGHLIGHT = (70, 100, 150)
MESSAGE_COLOR = (100, 200, 255)

# 物理参数
GRAVITY = 0.5
FPS = 60
ELASTICITY = 1.0  # 完全弹性碰撞
FRICTION = 1.0  # 无摩擦（完全弹性碰撞）

# 字体 - 使用SimHei中文字体
try:
    font = pygame.font.SysFont("SimHei", 24)
    title_font = pygame.font.SysFont("SimHei", 36)
    small_font = pygame.font.SysFont("SimHei", 20)
except:
    font = pygame.font.SysFont(None, 24)
    title_font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 20)

# 控制面板区域定义 - 增大面板高度解决重叠问题
PANEL_WIDTH = 260
PANEL_HEIGHT = 350  # 增加高度
PANEL_X = WIDTH - PANEL_WIDTH - 20
PANEL_Y = 20
panel_rect = pygame.Rect(PANEL_X, PANEL_Y, PANEL_WIDTH, PANEL_HEIGHT)


class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = 0
        self.selected = False
        self.dragging = False
        self.resizing = False
        self.rotating = False
        self.resize_edge = None
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.original_width = width
        self.original_height = height
        self.original_mouse_pos = (0, 0)
        self.original_corners = []

    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.width, self.height)
        rect.center = (self.x, self.y)

        obstacle_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        color = OBSTACLE_HIGHLIGHT if self.selected else OBSTACLE_COLOR
        pygame.draw.rect(obstacle_surface, color, (0, 0, self.width, self.height), 0, 5)
        pygame.draw.rect(obstacle_surface, UI_BORDER, (0, 0, self.width, self.height), 2, 5)

        rotated_surface = pygame.transform.rotate(obstacle_surface, self.rotation)
        rotated_rect = rotated_surface.get_rect(center=(self.x, self.y))

        surface.blit(rotated_surface, rotated_rect.topleft)

        if self.selected:
            pygame.draw.circle(surface, (255, 255, 0), (int(self.x), int(self.y)), 5)

            for i, point in enumerate(self.get_corners()):
                color = (0, 255, 0) if i == self.resize_edge else (255, 255, 0)
                pygame.draw.circle(surface, color, (int(point[0]), int(point[1])), 6)

    def get_corners(self):
        corners = [
            (self.x - self.width / 2, self.y - self.height / 2),
            (self.x + self.width / 2, self.y - self.height / 2),
            (self.x + self.width / 2, self.y + self.height / 2),
            (self.x - self.width / 2, self.y + self.height / 2)
        ]

        angle = math.radians(-self.rotation)
        rotated_corners = []
        for x, y in corners:
            dx = x - self.x
            dy = y - self.y
            new_x = dx * math.cos(angle) - dy * math.sin(angle) + self.x
            new_y = dx * math.sin(angle) + dy * math.cos(angle) + self.y
            rotated_corners.append((new_x, new_y))

        return rotated_corners

    def contains_point(self, point):
        px, py = point
        angle = math.radians(self.rotation)
        dx = px - self.x
        dy = py - self.y
        local_x = dx * math.cos(angle) - dy * math.sin(angle)
        local_y = dx * math.sin(angle) + dy * math.cos(angle)
        return (-self.width / 2 <= local_x <= self.width / 2 and
                -self.height / 2 <= local_y <= self.height / 2)

    def get_edge_at_point(self, point, threshold=10):
        corners = self.get_corners()
        for i, corner in enumerate(corners):
            if math.sqrt((point[0] - corner[0]) ** 2 + (point[1] - corner[1]) ** 2) < threshold:
                return i
        return None


class Ball:
    def __init__(self, x, y, radius=15):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = 0
        self.vy = 0
        self.selected = False
        self.dragging = False
        self.initial_velocity = 5
        self.initial_angle = 90  # 角度，0表示向右，90表示向下
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.original_vx = 0
        self.original_vy = 0
        self.temp_velocity = self.initial_velocity  # 临时保存滑块设置的速度
        self.temp_angle = self.initial_angle  # 临时保存滑块设置的角度

    def update(self):
        if self.selected or self.dragging:
            return

        # 应用重力
        self.vy += GRAVITY

        # 更新位置
        self.x += self.vx
        self.y += self.vy

        # 边界碰撞（完全弹性）
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx * ELASTICITY
        elif self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vx = -self.vx * ELASTICITY

        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy * ELASTICITY
        elif self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy * ELASTICITY

    def draw(self, surface):
        color = BALL_HIGHLIGHT if (self.selected or self.dragging) else BALL_COLOR
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, UI_BORDER, (int(self.x), int(self.y)), self.radius, 2)

        # 绘制速度方向指示器
        if self.selected:
            angle = math.radians(self.temp_angle)  # 使用临时角度
            end_x = self.x + math.cos(angle) * 30
            end_y = self.y + math.sin(angle) * 30
            pygame.draw.line(surface, (255, 255, 0), (self.x, self.y), (end_x, end_y), 2)
            pygame.draw.circle(surface, (255, 255, 0), (int(end_x), int(end_y)), 5)

    def contains_point(self, point):
        distance = math.sqrt((point[0] - self.x) ** 2 + (point[1] - self.y) ** 2)
        return distance <= self.radius

    def set_initial_velocity(self):
        angle = math.radians(self.initial_angle)
        self.vx = math.cos(angle) * self.initial_velocity
        self.vy = math.sin(angle) * self.initial_velocity

    def stop_movement(self):
        self.original_vx = self.vx
        self.original_vy = self.vy
        self.vx = 0
        self.vy = 0

    def resume_movement(self):
        self.vx = self.original_vx
        self.vy = self.original_vy

    def apply_temporary_settings(self):
        """将临时设置应用到小球 - 修改后直接设置当前速度"""
        self.initial_velocity = self.temp_velocity
        self.initial_angle = self.temp_angle

        # 直接设置当前速度
        angle = math.radians(self.initial_angle)
        self.vx = math.cos(angle) * self.initial_velocity
        self.vy = math.sin(angle) * self.initial_velocity


class Slider:
    def __init__(self, x, y, width, min_val, max_val, initial_val, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = 20
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.label = label
        self.dragging = False

    def draw(self, surface):
        # 绘制标签
        label_text = font.render(f"{self.label}: {self.value:.1f}", True, TEXT_COLOR)
        surface.blit(label_text, (self.x, self.y - 25))

        # 绘制滑块背景
        pygame.draw.rect(surface, SLIDER_BG, (self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(surface, UI_BORDER, (self.x, self.y, self.width, self.height), 2, 10)

        # 计算滑块位置
        pos_x = self.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.width

        # 绘制滑块
        pygame.draw.circle(surface, SLIDER_FG, (int(pos_x), int(self.y + self.height / 2)), 12)

    def handle_event(self, event, offset=(0, 0)):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            # 减去面板偏移
            mouse_x -= offset[0]
            mouse_y -= offset[1]
            # 检查是否点击在滑块上
            pos_x = self.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.width
            if math.sqrt((mouse_x - pos_x) ** 2 + (mouse_y - (self.y + self.height / 2)) ** 2) <= 12:
                self.dragging = True
                return True

        elif event.type == MOUSEBUTTONUP and event.button == 1:
            self.dragging = False

        elif event.type == MOUSEMOTION and self.dragging:
            mouse_x, mouse_y = event.pos
            # 减去面板偏移
            mouse_x -= offset[0]
            mouse_y -= offset[1]
            # 更新滑块值
            relative_x = max(0, min(mouse_x - self.x, self.width))
            self.value = self.min_val + (relative_x / self.width) * (self.max_val - self.min_val)
            return True

        return False


class PhysicsSimulator:
    def __init__(self):
        self.obstacles = []
        self.balls = []
        self.selected_object = None
        self.menu_active = False
        self.menu_pos = (0, 0)
        self.menu_options = ["添加障碍物", "添加小球"]
        self.selected_option = None
        # 修复：滑块位置使用面板内相对坐标，并调整垂直间距
        self.ball_velocity_slider = Slider(30, 120, 200, 0, 20, 5, "初速度")
        self.ball_angle_slider = Slider(30, 190, 200, 0, 360, 90, "角度")
        self.show_help = True
        self.paused = False
        self.grid_size = 40
        self.collision_debug = []
        self.message = ""
        self.message_timer = 0
        self.click_to_release = False  # 标记需要点击释放小球
        self.dragging_ball = None  # 当前正在拖动的小球

    def show_message(self, text, duration=120):
        self.message = text
        self.message_timer = duration

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 右键菜单 - 只在没有选中物体或选中障碍物时显示
            if event.type == MOUSEBUTTONDOWN and event.button == 3:  # 右键
                # 检查是否点击在小球上
                clicked_on_ball = False
                for ball in self.balls:
                    if ball.contains_point(event.pos):
                        clicked_on_ball = True
                        break

                # 如果没有点击在小球上，显示菜单
                if not clicked_on_ball:
                    self.menu_active = True
                    self.menu_pos = event.pos

            # 左键点击
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos

                # 检查是否点击了菜单
                if self.menu_active:
                    for i, option in enumerate(self.menu_options):
                        option_rect = pygame.Rect(self.menu_pos[0], self.menu_pos[1] + i * 40, 150, 35)
                        if option_rect.collidepoint(mouse_pos):
                            self.selected_option = i
                            self.menu_active = False
                            if i == 0:  # 添加障碍物
                                self.add_obstacle(mouse_pos[0], mouse_pos[1])
                                self.show_message("已添加障碍物 - 可拖动、旋转和缩放")
                            elif i == 1:  # 添加小球
                                self.add_ball(mouse_pos[0], mouse_pos[1])
                                self.show_message("已添加小球 - 可设置初速度和方向")
                            break
                    else:
                        self.menu_active = False
                        self.selected_option = None

                # 检查是否点击了物体
                else:
                    # 检查是否在控制面板上
                    if panel_rect.collidepoint(mouse_pos):
                        # 在控制面板上点击，不处理物体选择
                        pass
                    else:
                        # 检查是否需要释放小球
                        if self.click_to_release and isinstance(self.selected_object, Ball):
                            # 应用滑块设置到小球
                            self.selected_object.apply_temporary_settings()
                            self.deselect_ball()
                            self.click_to_release = False
                            return

                        prev_selected = self.selected_object
                        self.deselect_all()

                        # 先检查球
                        for ball in self.balls:
                            if ball.contains_point(mouse_pos):
                                ball.selected = True
                                self.selected_object = ball
                                ball.drag_offset_x = ball.x - mouse_pos[0]
                                ball.drag_offset_y = ball.y - mouse_pos[1]

                                # 停止小球运动
                                ball.stop_movement()
                                # 设置滑块为当前小球的临时值
                                self.ball_velocity_slider.value = ball.temp_velocity
                                self.ball_angle_slider.value = ball.temp_angle

                                self.show_message("已选中小球 - 可调整初速度和方向")
                                # 标记下次点击需要释放
                                self.click_to_release = True
                                break

                        # 再检查障碍物
                        else:
                            for obstacle in self.obstacles:
                                if obstacle.contains_point(mouse_pos):
                                    obstacle.selected = True
                                    self.selected_object = obstacle
                                    obstacle.dragging = True
                                    obstacle.drag_offset_x = obstacle.x - mouse_pos[0]
                                    obstacle.drag_offset_y = obstacle.y - mouse_pos[1]

                                    # 检查是否点击了边缘
                                    edge = obstacle.get_edge_at_point(mouse_pos)
                                    if edge is not None:
                                        obstacle.resizing = True
                                        obstacle.resize_edge = edge
                                        obstacle.original_width = obstacle.width
                                        obstacle.original_height = obstacle.height
                                        obstacle.original_mouse_pos = mouse_pos
                                        obstacle.original_corners = obstacle.get_corners()
                                        self.show_message("已选中障碍物边缘 - 拖动可缩放")
                                    else:
                                        self.show_message("已选中障碍物 - 可拖动和旋转")
                                    break

            # 鼠标释放
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                if isinstance(self.selected_object, Obstacle):
                    self.selected_object.dragging = False
                    self.selected_object.resizing = False
                    self.selected_object.rotating = False
                    self.show_message("已释放障碍物")
                elif self.dragging_ball:
                    # 结束小球拖动
                    self.dragging_ball.dragging = False
                    self.dragging_ball = None

            # 鼠标滚轮 - 旋转障碍物（修正旋转方向）
            elif event.type == MOUSEWHEEL:
                if isinstance(self.selected_object, Obstacle):
                    # 使用负值修正旋转方向
                    self.selected_object.rotation += event.y * -5
                    if self.selected_object.rotation < 0:
                        self.selected_object.rotation += 360
                    elif self.selected_object.rotation >= 360:
                        self.selected_object.rotation -= 360
                    self.show_message(f"障碍物旋转角度: {self.selected_object.rotation:.1f}°")

            # 键盘事件
            elif event.type == KEYDOWN:
                if event.key == K_h:
                    self.show_help = not self.show_help
                    self.show_message(f"帮助信息: {'已显示' if self.show_help else '已隐藏'}")
                elif event.key == K_SPACE:
                    self.paused = not self.paused
                    self.show_message(f"模拟: {'已暂停' if self.paused else '已继续'}")
                elif event.key == K_c:
                    self.balls.clear()
                    self.show_message("已清除所有小球")
                elif event.key == K_r:
                    self.obstacles.clear()
                    self.show_message("已清除所有障碍物")
                elif event.key == K_ESCAPE:
                    self.deselect_all()
                    self.show_message("已取消选择所有物体")
                elif event.key == K_d:
                    if self.selected_object:
                        if isinstance(self.selected_object, Ball) and self.selected_object in self.balls:
                            self.balls.remove(self.selected_object)
                            self.show_message("已删除选中小球")
                        elif isinstance(self.selected_object, Obstacle) and self.selected_object in self.obstacles:
                            self.obstacles.remove(self.selected_object)
                            self.show_message("已删除选中障碍物")
                        self.deselect_all()

            # 处理滑块事件 - 修复：传递面板偏移坐标
            if isinstance(self.selected_object, Ball) and self.selected_object.selected:
                # 传递面板偏移坐标
                if self.ball_velocity_slider.handle_event(event, (PANEL_X, PANEL_Y)):
                    # 更新小球的临时速度
                    self.selected_object.temp_velocity = self.ball_velocity_slider.value
                    self.show_message(f"初速度: {self.selected_object.temp_velocity:.1f}")
                if self.ball_angle_slider.handle_event(event, (PANEL_X, PANEL_Y)):
                    # 更新小球的临时角度
                    self.selected_object.temp_angle = self.ball_angle_slider.value
                    self.show_message(f"角度: {self.selected_object.temp_angle:.1f}°")

        # 处理小球拖动（在事件循环外）
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pressed:
            # 检查是否在拖动小球
            if not self.dragging_ball and not self.menu_active and not panel_rect.collidepoint(mouse_pos):
                for ball in self.balls:
                    if ball.contains_point(mouse_pos) and not ball.selected:
                        # 开始拖动小球
                        ball.dragging = True
                        ball.drag_offset_x = ball.x - mouse_pos[0]
                        ball.drag_offset_y = ball.y - mouse_pos[1]
                        self.dragging_ball = ball
                        # 停止小球运动
                        ball.stop_movement()
                        self.show_message("正在拖动小球 - 释放鼠标放置")
                        break

        # 更新拖动小球的位置
        if self.dragging_ball:
            self.dragging_ball.x = mouse_pos[0] + self.dragging_ball.drag_offset_x
            self.dragging_ball.y = mouse_pos[1] + self.dragging_ball.drag_offset_y

    def add_obstacle(self, x, y):
        new_obstacle = Obstacle(x, y, 80, 50)
        self.obstacles.append(new_obstacle)
        self.deselect_all()
        new_obstacle.selected = True
        self.selected_object = new_obstacle

    def add_ball(self, x, y):
        new_ball = Ball(x, y)
        new_ball.set_initial_velocity()
        self.balls.append(new_ball)
        self.deselect_all()
        new_ball.selected = True
        self.selected_object = new_ball

        # 设置滑块初始值
        self.ball_velocity_slider.value = new_ball.initial_velocity
        self.ball_angle_slider.value = new_ball.initial_angle
        # 设置临时值
        new_ball.temp_velocity = new_ball.initial_velocity
        new_ball.temp_angle = new_ball.initial_angle

        # 新添加的小球自动停止
        new_ball.stop_movement()
        self.click_to_release = True

    def deselect_ball(self):
        if isinstance(self.selected_object, Ball):
            # 应用临时设置
            self.selected_object.apply_temporary_settings()
            self.selected_object.selected = False
            # 不再恢复原始运动，因为已经应用了新速度
            self.selected_object = None
            self.show_message("已释放小球 - 开始运动")

    def deselect_all(self):
        # 取消选择所有物体
        for obstacle in self.obstacles:
            obstacle.selected = False
        for ball in self.balls:
            ball.selected = False
        self.selected_object = None
        self.click_to_release = False

    def update(self):
        # 更新消息计时器
        if self.message_timer > 0:
            self.message_timer -= 1

        if self.paused:
            return

        # 更新小球位置
        for ball in self.balls:
            ball.update()

        # 更新障碍物位置
        for obstacle in self.obstacles:
            if obstacle.dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                obstacle.x = mouse_x + obstacle.drag_offset_x
                obstacle.y = mouse_y + obstacle.drag_offset_y

            # 处理障碍物缩放 - 改进版（中心不动）
            if obstacle.resizing and obstacle.resize_edge is not None:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # 获取原始角点
                corners = obstacle.original_corners
                target_corner = corners[obstacle.resize_edge]

                # 计算新的角点位置
                new_corners = list(corners)
                new_corners[obstacle.resize_edge] = (mouse_x, mouse_y)

                # 计算新的中心点
                center_x = sum(c[0] for c in new_corners) / 4
                center_y = sum(c[1] for c in new_corners) / 4

                # 更新障碍物位置
                obstacle.x = center_x
                obstacle.y = center_y

                # 计算新的宽度和高度
                # 从中心点到每个角点的距离
                dist_x = max(abs(c[0] - center_x) for c in new_corners)
                dist_y = max(abs(c[1] - center_y) for c in new_corners)

                # 更新尺寸
                obstacle.width = max(20, dist_x * 2)
                obstacle.height = max(20, dist_y * 2)

        # 检测球与障碍物的碰撞 - 完全弹性
        self.collision_debug = []  # 清空碰撞调试信息
        for ball in self.balls:
            for obstacle in self.obstacles:
                # 改进的碰撞检测 - 使用分离轴定理（SAT）处理旋转矩形
                self.check_ball_obstacle_collision(ball, obstacle)

        # 检测球与球之间的碰撞 - 完全弹性
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball1 = self.balls[i]
                ball2 = self.balls[j]

                dx = ball2.x - ball1.x
                dy = ball2.y - ball1.y
                distance = math.sqrt(dx * dx + dy * dy)

                if distance < ball1.radius + ball2.radius:
                    # 碰撞发生
                    angle = math.atan2(dy, dx)

                    # 计算碰撞前的速度分量
                    v1x = ball1.vx
                    v1y = ball1.vy
                    v2x = ball2.vx
                    v2y = ball2.vy

                    # 完全弹性碰撞公式
                    # 计算碰撞方向单位向量
                    nx = dx / distance
                    ny = dy / distance

                    # 计算相对速度
                    dvx = v2x - v1x
                    dvy = v2y - v1y

                    # 计算速度在碰撞方向上的投影
                    velocity_along_normal = dvx * nx + dvy * ny

                    # 完全弹性碰撞，速度交换
                    impulse = 2.0 * velocity_along_normal

                    # 应用碰撞
                    ball1.vx += impulse * nx * ELASTICITY
                    ball1.vy += impulse * ny * ELASTICITY
                    ball2.vx -= impulse * nx * ELASTICITY
                    ball2.vy -= impulse * ny * ELASTICITY

                    # 防止球粘连
                    overlap = (ball1.radius + ball2.radius - distance) / 2
                    ball1.x -= overlap * nx
                    ball1.y -= overlap * ny
                    ball2.x += overlap * nx
                    ball2.y += overlap * ny

    def check_ball_obstacle_collision(self, ball, obstacle):
        # 获取障碍物的角点
        corners = obstacle.get_corners()

        # 将障碍物视为多边形，检查每条边
        for i in range(len(corners)):
            # 边的两个端点
            p1 = corners[i]
            p2 = corners[(i + 1) % len(corners)]

            # 计算边向量
            edge = (p2[0] - p1[0], p2[1] - p1[1])

            # 计算边的长度
            length = math.sqrt(edge[0] ** 2 + edge[1] ** 2)
            if length == 0:
                continue

            # 归一化边向量
            edge = (edge[0] / length, edge[1] / length)

            # 计算边的法向量（垂直于边）
            normal = (-edge[1], edge[0])

            # 计算球心到边的投影
            ball_to_p1 = (ball.x - p1[0], ball.y - p1[1])
            projection = ball_to_p1[0] * normal[0] + ball_to_p1[1] * normal[1]

            # 如果投影小于球的半径，则可能发生碰撞
            if abs(projection) < ball.radius:
                # 计算球心到边的距离
                distance = abs(projection)

                # 计算球与边的接触点
                contact_point = (
                    ball.x - projection * normal[0],
                    ball.y - projection * normal[1]
                )

                # 检查接触点是否在边的范围内
                edge_to_contact = (contact_point[0] - p1[0], contact_point[1] - p1[1])
                dot = edge_to_contact[0] * edge[0] + edge_to_contact[1] * edge[1]

                if 0 <= dot <= length:
                    # 计算重叠量（增加1.0的额外距离防止卡住）
                    overlap = ball.radius - distance + 1.0

                    # 确保法线指向外部
                    # 计算球心到接触点的向量
                    ball_to_contact = (contact_point[0] - ball.x, contact_point[1] - ball.y)
                    dot_normal = ball_to_contact[0] * normal[0] + ball_to_contact[1] * normal[1]

                    # 如果点积为正，说明法线指向球内部，需要反转
                    if dot_normal > 0:
                        normal = (-normal[0], -normal[1])

                    # 将球移出障碍物
                    ball.x += overlap * normal[0]
                    ball.y += overlap * normal[1]

                    # 计算速度在法线方向上的分量
                    dot_product = ball.vx * normal[0] + ball.vy * normal[1]

                    # 完全弹性碰撞：速度在法线方向的分量反向
                    ball.vx -= 2 * dot_product * normal[0] * ELASTICITY
                    ball.vy -= 2 * dot_product * normal[1] * ELASTICITY

                    # 添加调试信息
                    self.collision_debug.append({
                        'type': 'ball_obstacle',
                        'ball': (ball.x, ball.y),
                        'contact': contact_point,
                        'normal': normal
                    })
                    return

    def draw(self, surface):
        # 绘制背景
        surface.fill(BACKGROUND)

        # 绘制网格
        for x in range(0, WIDTH, self.grid_size):
            pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, self.grid_size):
            pygame.draw.line(surface, GRID_COLOR, (0, y), (WIDTH, y), 1)

        # 绘制物体
        for obstacle in self.obstacles:
            obstacle.draw(surface)

        for ball in self.balls:
            ball.draw(surface)

        # 绘制碰撞调试信息
        for debug in self.collision_debug:
            pygame.draw.circle(surface, (0, 255, 0), (int(debug['contact'][0]), int(debug['contact'][1])), 4)
            pygame.draw.line(
                surface, (0, 255, 0),
                (debug['contact'][0], debug['contact'][1]),
                (debug['contact'][0] + debug['normal'][0] * 30, debug['contact'][1] + debug['normal'][1] * 30),
                2
            )

        # 绘制菜单
        if self.menu_active:
            menu_surface = pygame.Surface((150, len(self.menu_options) * 40), pygame.SRCALPHA)
            menu_surface.fill(MENU_BG)

            for i, option in enumerate(self.menu_options):
                if i == self.selected_option:
                    pygame.draw.rect(menu_surface, MENU_HIGHLIGHT, (0, i * 40, 150, 40))

                text = font.render(option, True, TEXT_COLOR)
                text_rect = text.get_rect(center=(75, i * 40 + 20))
                menu_surface.blit(text, text_rect)

            pygame.draw.rect(menu_surface, UI_BORDER, (0, 0, 150, len(self.menu_options) * 40), 2)
            surface.blit(menu_surface, self.menu_pos)

        # 绘制控制面板（始终显示）
        panel = pygame.Surface((PANEL_WIDTH, PANEL_HEIGHT), pygame.SRCALPHA)
        panel.fill(UI_BG)
        pygame.draw.rect(panel, UI_BORDER, (0, 0, PANEL_WIDTH, PANEL_HEIGHT), 2)

        # 面板标题
        title = title_font.render("控制面板", True, TEXT_COLOR)
        panel.blit(title, (PANEL_WIDTH // 2 - title.get_width() // 2, 15))

        # 状态信息 - 增加垂直间距
        status = font.render(f"小球: {len(self.balls)}", True, TEXT_COLOR)
        panel.blit(status, (20, 50))

        status = font.render(f"障碍物: {len(self.obstacles)}", True, TEXT_COLOR)
        panel.blit(status, (20, 80))

        # 绘制滑块（如果选中小球）
        if isinstance(self.selected_object, Ball) and self.selected_object.selected:
            # 直接在面板表面绘制滑块
            self.ball_velocity_slider.draw(panel)
            self.ball_angle_slider.draw(panel)

            # 添加释放提示 - 调整位置
            release_hint = small_font.render("点击场景应用设置", True, (180, 255, 180))
            panel.blit(release_hint, (PANEL_WIDTH // 2 - release_hint.get_width() // 2, 240))  # 位置下移
        else:
            # 显示提示信息 - 调整位置
            hint = font.render("选中小球显示设置", True, (180, 180, 220))
            panel.blit(hint, (PANEL_WIDTH // 2 - hint.get_width() // 2, 130))

        # 控制说明 - 增加垂直间距
        pygame.draw.line(panel, UI_BORDER, (20, 270), (PANEL_WIDTH - 20, 270), 1)  # 位置下移
        instructions = [
            "空格键: 暂停/继续",
            "H键: 显示/隐藏帮助",
            "C键: 清除所有小球",
            "R键: 清除障碍物",
            "ESC键: 取消选择",
            "D键: 删除选中物体",
            "拖动: 直接拖动小球移动"
        ]

        # 增加行间距
        for i, instruction in enumerate(instructions):
            text = small_font.render(instruction, True, TEXT_COLOR)
            panel.blit(text, (20, 280 + i * 25))  # 增加行高

        surface.blit(panel, (PANEL_X, PANEL_Y))

        # 绘制帮助信息
        if self.show_help:
            help_panel = pygame.Surface((400, 240), pygame.SRCALPHA)  # 增加高度
            help_panel.fill(UI_BG)
            pygame.draw.rect(help_panel, UI_BORDER, (0, 0, 400, 240), 2)

            help_title = title_font.render("操作指南", True, TEXT_COLOR)
            help_panel.blit(help_title, (200 - help_title.get_width() // 2, 15))

            help_text = [
                "右键: 在空白处添加物体",
                "左键: 选择/拖动物体",
                "滚轮: 旋转障碍物",
                "拖动边缘: 缩放障碍物",
                "小球: 选中小球后设置初速度",
                "释放: 在场景中点击应用设置",
                "拖动: 直接拖动小球改变位置",
                "碰撞: 完全弹性碰撞",
                "提示: 右下角有操作提示"
            ]

            # 增加行间距
            for i, text in enumerate(help_text):
                text_surf = small_font.render(text, True, TEXT_COLOR)
                help_panel.blit(text_surf, (20, 50 + i * 22))  # 增加行高

            surface.blit(help_panel, (20, 20))

        # 绘制暂停状态
        if self.paused:
            pause_surface = pygame.Surface((200, 60), pygame.SRCALPHA)
            pause_surface.fill((0, 0, 0, 150))
            pygame.draw.rect(pause_surface, UI_BORDER, (0, 0, 200, 60), 2)

            pause_text = title_font.render("模拟已暂停", True, (255, 100, 100))
            pause_surface.blit(pause_text, (100 - pause_text.get_width() // 2, 15))

            surface.blit(pause_surface, (WIDTH // 2 - 100, HEIGHT // 2 - 30))

        # 绘制选中小球状态
        if any(ball.selected for ball in self.balls):
            status_surface = pygame.Surface((300, 40), pygame.SRCALPHA)
            status_surface.fill((0, 50, 0, 150))
            pygame.draw.rect(status_surface, (0, 150, 0), (0, 0, 300, 40), 2)

            status_text = font.render("小球已选中 - 点击场景应用设置", True, (100, 255, 100))
            status_surface.blit(status_text, (150 - status_text.get_width() // 2, 10))

            surface.blit(status_surface, (WIDTH // 2 - 150, HEIGHT - 50))

        # 绘制拖动小球状态
        if self.dragging_ball:
            status_surface = pygame.Surface((300, 40), pygame.SRCALPHA)
            status_surface.fill((50, 50, 0, 150))
            pygame.draw.rect(status_surface, (150, 150, 0), (0, 0, 300, 40), 2)

            status_text = font.render("正在拖动小球 - 释放鼠标放置", True, (255, 255, 100))
            status_surface.blit(status_text, (150 - status_text.get_width() // 2, 10))

            surface.blit(status_surface, (WIDTH // 2 - 150, HEIGHT - 50))

        # 绘制操作提示
        if self.message_timer > 0:
            msg_surface = pygame.Surface((WIDTH - 40, 30), pygame.SRCALPHA)
            msg_surface.fill((0, 0, 0, 150))
            pygame.draw.rect(msg_surface, (100, 180, 255), (0, 0, WIDTH - 40, 30), 1)

            msg_text = font.render(self.message, True, MESSAGE_COLOR)
            msg_surface.blit(msg_text, ((WIDTH - 40) // 2 - msg_text.get_width() // 2, 5))

            surface.blit(msg_surface, (20, HEIGHT - 40))


# 创建模拟器
simulator = PhysicsSimulator()
clock = pygame.time.Clock()

# 添加初始物体
simulator.add_obstacle(200, 300)
simulator.add_obstacle(700, 400)
simulator.add_ball(400, 200)
simulator.add_ball(600, 150)

# 显示欢迎消息
simulator.show_message("欢迎使用物理模拟器 - 右键添加物体，左键选择物体，选中小球后设置初速度", 180)

# 主循环
while True:
    simulator.handle_events()
    simulator.update()

    simulator.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)