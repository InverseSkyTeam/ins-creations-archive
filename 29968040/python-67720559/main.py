import pygame
import sys


pygame.init()
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

def find_intersection_x(a, b, m):
    # 计算点a到点b的直线与竖直线x=m的交点纵坐标
    x1, y1 = a
    x2, y2 = b
    slope = (y2 - y1) / (x2 - x1)
    y_intersect = y1 + slope * (m - x1)

    return (m, y_intersect)


def find_intersection_y(a, b, m):
    # 计算点a到点b的直线与水平线y=m的交点横坐标
    x1, y1 = a
    x2, y2 = b
    if x2 == x1:
        return (x1, m)
    slope = (y2 - y1) / (x2 - x1)
    x_intersect = x1 + (m - y1) / slope
    
    return (x_intersect, m)


def find_slant_border(a, a_border, b, b_border, w, h):
    flag_a = 0 <= a_border[0][1] <= h-1, 0 <= a_border[1][0] <= w-1
    flag_b = 0 <= b_border[0][1] <= h-1, 0 <= b_border[1][0] <= w-1
    if flag_a[0] == flag_b[0] == True:
        return (a, a_border[0], b_border[0], b)
    elif flag_a[1] == flag_b[1] == True:
        return (a, a_border[1], b_border[1], b)
    elif flag_a[0] == flag_b[1] == True:
        return (a, a_border[0], (a_border[0][0], b_border[1][1]), b_border[1], b)
    elif flag_a[1] == flag_b[0] == True:
        return (a, a_border[1], (a_border[1][0], b_border[0][1]), b_border[0], b)
    else:
        raise ValueError


def ray_tracing_2d(w, h, origin_wall_rect, origin_people_pos, offset_x=0, offset_y=0):
    mask_surface = pygame.Surface((w, h), pygame.SRCALPHA).convert_alpha()
    wall_rect = []
    surface_rect = pygame.Rect(0, 0, w, h)
    people_x, people_y = people_pos = origin_people_pos[0] + offset_x, origin_people_pos[1] + offset_y
    debug = False
    
    for origin_wall in origin_wall_rect:
        wall = origin_wall.move(offset_x, offset_y).clip(surface_rect)
        if wall.w == 0 or wall.h == 0:
            continue
        if wall.collidepoint(people_x, people_y):  # 若角色在墙壁内部
            mask_surface.fill((0, 0, 0, 128))
            mask_surface.fill((0, 0, 0, 0), rect=wall)
            return mask_surface
        
        wall_rect.append(wall)
        
   
    for wall in wall_rect:
        wall_left, wall_right = wall.x, wall.x + wall.w - 1
        wall_top, wall_bottom = wall.y, wall.y + wall.h - 1
        p_tl = (wall_left,  wall_top)  # 墙的左上角点
        p_tr = (wall_right, wall_top)  # 墙的右上角点
        p_bl = (wall_left,  wall_bottom)  # 墙的左下角点
        p_br = (wall_right, wall_bottom)  # 墙的右下角点
        
        render_vertex = []
        if wall_left <= people_x <= wall_right:  # 角色在墙的上/下方
            if wall_bottom < people_y:  # 墙在上方
                p1, p2 = p_bl, p_br
                limit_vertical = 0
            elif people_y < wall_top:  # 墙在下方
                p1, p2 = p_tl, p_tr
                limit_vertical = h - 1
            p1_border_y = find_intersection_y(people_pos, p1, limit_vertical)
            p2_border_y = find_intersection_y(people_pos, p2, limit_vertical)
            if 0 <= p1_border_y[0] <= w-1:
                p1_border = (p1_border_y,)
            else:
                p1_border = (find_intersection_x(people_pos, p1, 0), (0, limit_vertical))
            if 0 <= p2_border_y[0] <= w-1:
                p2_border = (p2_border_y,)
            else:
                p2_border = ((w-1, limit_vertical), find_intersection_x(people_pos, p2, w-1))
            render_vertex = p1_border + p2_border + (p2, p1)
        elif wall_top <= people_y <= wall_bottom:  # 角色在墙的左/右方
            if wall_right < people_x:  # 墙在左边
                p1, p2 = p_tr, p_br
                limit_horizontal = 0
            elif people_x < wall_left:  # 墙在右边
                p1, p2 = p_tl, p_bl
                limit_horizontal = w - 1
            p1_border_x = find_intersection_x(people_pos, p1, limit_horizontal)
            p2_border_x = find_intersection_x(people_pos, p2, limit_horizontal)
            if 0 <= p1_border_x[1] <= h-1:
                p1_border = (p1_border_x,)
            else:
                p1_border = (find_intersection_y(people_pos, p1, 0), (limit_horizontal, 0))
            if 0 <= p2_border_x[1] <= h-1:
                p2_border = (p2_border_x,)
            else:
                p2_border = ((limit_horizontal, h-1), find_intersection_y(people_pos, p2, h-1))
            render_vertex = p1_border + p2_border + (p2, p1)
        else:  # 处理四个角落方向（左上，右下，右上，左下）
            if people_x < p_tl[0] and people_y < p_tl[1]:  # 墙在右下角
                p0, p1, p2 = p_tl, p_tr, p_bl
                limit_x, limit_y = w-1, h-1
            elif people_x > p_tr[0] and people_y < p_tr[1]:  # 墙在左下角
                p0, p1, p2 = p_tr, p_tl, p_br
                limit_x, limit_y = 0, h-1
            elif people_x < p_bl[0] and people_y > p_bl[1]:  # 墙在右上角
                p0, p1, p2 = p_bl, p_br, p_tl
                limit_x, limit_y = w-1, 0
            elif people_x > p_br[0] and people_y > p_br[1]:  # 墙在左上角
                p0, p1, p2 = p_br, p_bl, p_tr
                limit_x, limit_y = 0, 0
                
            p1_border = (find_intersection_x(people_pos, p1, limit_x), 
                         find_intersection_y(people_pos, p1, limit_y))
            p2_border = (find_intersection_x(people_pos, p2, limit_x), 
                         find_intersection_y(people_pos, p2, limit_y))
            render_vertex = find_slant_border(p1, p1_border, p2, p2_border, w, h) + (p0,)

        pygame.draw.polygon(mask_surface, (0, 0, 0, 128), render_vertex)
        if debug:
            pygame.draw.polygon(mask_surface, (0, 255, 255, 255), render_vertex, width=1)
    return mask_surface


people_rect = pygame.Rect(100, 400, 50, 50)
all_wall_rects = [
    pygame.Rect(50, 50, 200, 200),    # 原始矩形
    pygame.Rect(500, 500, 100, 100),  # 原始矩形
    pygame.Rect(120, 320, 150, 40),   # 新增
    pygame.Rect(400, 80, 80, 180),    # 新增
    pygame.Rect(600, 250, 160, 60),   # 新增
    pygame.Rect(200, 450, 50, 120),   # 新增
    pygame.Rect(700, 100, 30, 100),   # 新增
    pygame.Rect(300, 200, 120, 90),   # 新增
    pygame.Rect(50, 500, 200, 30),    # 新增
    pygame.Rect(450, 350, 70, 70),    # 新增
    pygame.Rect(150, 100, 40, 140),   # 新增
    pygame.Rect(550, 400, 100, 50)    # 新增
]

move_index = -1
font = pygame.font.SysFont(None, 30)
while True:
    fps_str = 'fps:' + str(round(clock.get_fps()))
    pygame.display.set_caption(fps_str)
    pygame_events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, _rect in enumerate(all_wall_rects + [people_rect]):
                if _rect.collidepoint(event.pos):
                    move_index = i
        if event.type == pygame.MOUSEMOTION and move_index >= 0:
            if move_index < len(all_wall_rects):
                all_wall_rects[move_index].move_ip(*event.rel)
            else:
                people_rect.move_ip(*event.rel)
        if event.type == pygame.MOUSEBUTTONUP:
            move_index = -1
            

    screen.fill((255, 255, 255))
    # screen.fill((235, 235, 235), (0, 0, screenWidth, screenHeight))
    
    pygame.draw.rect(screen, (0, 255, 0), people_rect)
    for _rect in all_wall_rects:
        pygame.draw.rect(screen, (255, 0, 0), _rect)
    mask = ray_tracing_2d(screenWidth, screenHeight, all_wall_rects, people_rect.center)
    screen.blit(mask, (0, 0))
    screen.blit(font.render(fps_str, True, (255, 0, 0)), (10, 10))
    
    pygame.display.flip()
    clock.tick(114514)
