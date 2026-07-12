import math
import pygame


def get_line_intersection(p0_x, p0_y, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    s10_x = p1_x - p0_x
    s10_y = p1_y - p0_y
    s32_x = p3_x - p2_x
    s32_y = p3_y - p2_y

    denom = s10_x * s32_y - s32_x * s10_y
    if denom == 0:  # 平行或共线
        return None
    denomPositive: bool = denom > 0

    s02_x = p0_x - p2_x
    s02_y = p0_y - p2_y
    s_numer = s10_x * s02_y - s10_y * s02_x
    if (s_numer < 0) == denomPositive:  # 参数是大于等于0且小于等于1的，分子分母必须同号且分子小于等于分母
        return None

    t_numer = s32_x * s02_y - s32_y * s02_x
    if (t_numer < 0) == denomPositive:
        return None

    if abs(s_numer) > abs(denom) or abs(t_numer) > abs(denom):
        return None
    # 有交点
    t = t_numer / denom
    i_x = p0_x + (t * s10_x)
    i_y = p0_y + (t * s10_y)

    return i_x, i_y, t


def trans(x, y, angle, tx, ty):
    cos_angle = math.cos(math.radians(angle))
    sin_angle = math.sin(math.radians(angle))
    return x * cos_angle - y * sin_angle + tx, y * cos_angle + x * sin_angle + ty


class Ray:
    def __init__(self, collision):
        self.collision = collision
        self.ray_x, self.ray_y, self.ray_z = None, None, None

    def update_ray(self, alpha, beta):
        rad_alpha, rad_beta = math.radians(alpha), math.radians(-beta)
        self.ray_x = math.cos(rad_beta) * math.sin(rad_alpha)
        self.ray_y = math.sin(rad_beta)
        self.ray_z = math.cos(rad_beta) * math.cos(rad_alpha)

    def ray_collision(self, tx, ty, tz, peoples):
        p1_x, p1_y, p1_z = tx + 1145 * self.ray_x, ty + 1145 * self.ray_y, tz + 1145 * self.ray_z
        min_dist = 114514
        for i in range(len(self.collision.collision_pos)):
            if (i + 1) % 2 == 1:
                p2, p3 = self.collision.collision_pos[i], self.collision.collision_pos[i + 1]
                res = get_line_intersection(tx, tz, p1_x, p1_z, *p2, *p3)
                if res:
                    min_dist = min(min_dist, (res[0] - tx)**2 + (res[1] - tz)**2)

        collision_people = None
        for people in peoples:
            if people.hp <= 0 or not people.is_show:
                continue
            new_angle = people.get_angle(tx, tz)
            p_s, p_e = trans(-3, 0, -new_angle, people.tx, people.tz), trans(3, 0, -new_angle, people.tx, people.tz)
            res = get_line_intersection(tx, tz, p1_x, p1_z, *p_s, *p_e)
            if res and min_dist > (res[0] - tx) ** 2 + (res[1] - tz) ** 2 and 0 < ty + res[2] * (p1_y - ty) <= 7.5:
                collision_people = people
        if collision_people:
            collision_people.send_hp = True

    def debug_ray(self, screen, tx, ty, tz, peoples):
        sf = pygame.Surface((200, 200))
        sf.fill((255,) * 3)
        for i in range(len(self.collision.collision_pos)):
            if (i + 1) % 2 == 1:
                p2_x, p2_y = self.collision.collision_pos[i]
                p3_x, p3_y = self.collision.collision_pos[i + 1]
                pygame.draw.line(sf, (0, )*3, (p2_x + 100, -p2_y + 100), (p3_x + 100, -p3_y + 100))
        p1_x, p1_y, p1_z = tx + 1145 * self.ray_x, ty + 1145 * self.ray_y, tz + 1145 * self.ray_z
        pygame.draw.line(sf, (255, 0, 0), (tx + 100, -tz + 100), (p1_x + 100, -p1_z + 100))

        for people in peoples:
            if people.hp <= 0 or not people.is_show:
                continue
            new_angle = people.get_angle(tx, tz)
            p_s, p_e = trans(-3, 0, -new_angle, people.tx, people.tz), trans(3, 0, -new_angle, people.tx, people.tz)
            pygame.draw.line(sf, (0, 0, 255), (p_s[0] + 100, -p_s[1] + 100), (p_e[0] + 100, -p_e[1] + 100))
        screen.blit(sf, (0, 0))
