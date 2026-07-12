import pygame
import numpy as np
import sys

# 初始化
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("多个点电荷的电场线（带方向）")

# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
ARROW_COLOR = (200, 200, 200)  # 箭头颜色

# ========== 点电荷定义 ==========
class Charge:
    def __init__(self, pos, q):
        self.pos = np.array(pos, dtype=float)
        self.q = q

# 示例：两个正电荷，一个负电荷
charges = [
    Charge((300, 300),  1),
    Charge((500, 300),  1),
    Charge((400, 450), -1),
]

K = 1.0  # 库仑常数

# ========== 电场计算 ==========
def electric_field(points, charges):
    """批量计算电场 (N,2) -> (N,2)"""
    E = np.zeros_like(points)
    for charge in charges:
        r_vec = points - charge.pos
        dist = np.linalg.norm(r_vec, axis=1)
        dist = np.maximum(dist, 1e-4)  # 防除零
        E += (K * charge.q / dist**3)[:, np.newaxis] * r_vec
    return E

# ========== 单条电场线追踪 ==========
def trace_field_line(start_point, charges, ds=1.0, max_steps=3000, stop_dist=8.0):
    path = [start_point.copy()]
    current = start_point.copy().astype(float)

    for _ in range(max_steps):
        E = electric_field(np.array([current]), charges)[0]
        norm = np.linalg.norm(E)
        if norm < 1e-12:
            break
        direction = E / norm
        next_point = current + direction * ds

        # 边界检查
        if not (0 <= next_point[0] < WIDTH and 0 <= next_point[1] < HEIGHT):
            path.append(next_point)
            break

        # 靠近负电荷时终止
        for ch in charges:
            if ch.q < 0 and np.linalg.norm(next_point - ch.pos) < stop_dist:
                path.append(next_point)
                return path  # 直接返回，不再继续

        path.append(next_point)
        current = next_point

    return path

# ========== 生成起始点 ==========
def generate_start_points(charges, n_lines=20, start_radius=10):
    points = []
    for ch in charges:
        if ch.q > 0:
            angles = np.linspace(0, 2*np.pi, n_lines, endpoint=False)
            for ang in angles:
                sp = ch.pos + start_radius * np.array([np.cos(ang), np.sin(ang)])
                if 0 <= sp[0] < WIDTH and 0 <= sp[1] < HEIGHT:
                    points.append(sp)
    return points

# ========== 绘制方向箭头 ==========
def draw_arrow(screen, pos, direction, size=8, color=ARROW_COLOR):
    """在 pos 处绘制一个指向 direction 的三角形箭头"""
    tip = pos + direction * size
    # 垂直向量
    perp = np.array([-direction[1], direction[0]])
    left = pos + perp * size * 0.4
    right = pos - perp * size * 0.4
    pygame.draw.polygon(screen, color, [tip, left, right])

# ========== 计算所有电场线 ==========
def compute_all_lines(charges):
    start_pts = generate_start_points(charges)
    lines = [trace_field_line(sp, charges) for sp in start_pts]
    return lines

field_lines = compute_all_lines(charges)

# ========== 主循环 ==========
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # 绘制电场线
    for line in field_lines:
        if len(line) > 1:
            # 画线条
            pygame.draw.lines(screen, WHITE, False, line, 1)

            # 每 20 像素画一个方向箭头
            arrow_spacing = 100  # 像素间隔
            # 转换成整数索引步长（因为 ds=1.0，点间隔约 1 像素）
            step = max(1, arrow_spacing)
            for i in range(0, len(line)-1, step):
                p1 = np.array(line[i])
                p2 = np.array(line[i+1])
                d = p2 - p1
                norm = np.linalg.norm(d)
                if norm > 1e-6:
                    draw_arrow(screen, p1, d/norm, size=8)

    # 绘制点电荷
    for ch in charges:
        color = RED if ch.q > 0 else BLUE
        radius = max(6, int(abs(ch.q) * 8))
        pygame.draw.circle(screen, color, ch.pos.astype(int), radius)
        # 正负号
        font = pygame.font.SysFont(None, 24)
        sign = '+' if ch.q > 0 else '-'
        text = font.render(sign, True, WHITE)
        text_rect = text.get_rect(center=ch.pos.astype(int))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()