import numpy as np
import math

class OBB:
    def __init__(self, center, axis, lengths):
        self.center = center  # 中心点
        self.axis = axis  # 轴向量
        self.lengths = lengths  # 边长
def obb_collision(obb1, obb2):
    diff = obb2.center - obb1.center
    for i in range(3):
        axis1 = obb1.axis[i]
        axis2 = obb2.axis[i]
        # 计算diff相对于obb1和obb2的基本坐标系
        t = np.dot(diff, axis1)
        u = np.dot(diff, axis2)
        # 计算投影距离
        projection1 = np.abs(t)
        projection2 = np.abs(u)
        # 判断投影是否重叠
        if projection1 > obb1.lengths[i] + obb2.lengths[i] or projection2 > obb1.lengths[i] + obb2.lengths[i]:
            return False
    return True

def rotate_around_axis(axis, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    # 创建对应旋转轴的旋转矩阵
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, cos_theta, -sin_theta],
                                    [0, sin_theta, cos_theta]])
    elif axis == 'y':
        rotation_matrix = np.array([[cos_theta, 0, sin_theta],
                                    [0, 1, 0],
                                    [-sin_theta, 0, cos_theta]])
    elif axis == 'z':
        rotation_matrix = np.array([[cos_theta, -sin_theta, 0],
                                    [sin_theta, cos_theta, 0],
                                    [0, 0, 1]])
    else:
        raise ValueError("Invalid rotation axis. Please use 'x', 'y', or 'z'.")
    return rotation_matrix

# 创建旋转矩阵，分别绕x轴、y轴和z轴旋转50度
rotation_matrix_x = rotate_around_axis('x', 50)
rotation_matrix_y = rotate_around_axis('y', 50)
rotation_matrix_z = rotate_around_axis('z', 50)
# 创建原始的OBB对象
obb_original = OBB(np.array([0, 0, 0]), [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])], [30, 30, 30])
# 将obb进行绕x轴旋转
obb_rotated_x = OBB(obb_original.center, [rotation_matrix_x.dot(axis) for axis in obb_original.axis], obb_original.lengths)
# 将obb_rotated_x进行绕y轴旋转
obb_rotated_y = OBB(obb_rotated_x.center, [rotation_matrix_y.dot(axis) for axis in obb_rotated_x.axis], obb_rotated_x.lengths)
# 将obb_rotated_y进行绕z轴旋转
obb_rotated_z = OBB(obb_rotated_y.center, [rotation_matrix_z.dot(axis) for axis in obb_rotated_y.axis], obb_rotated_y.lengths)
# 创建另一个OBB对象
obb2 = OBB(np.array([0, 0, 0]), [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])], [15, 15, 15])
# 调用碰撞检测函数，传入绕x、y、z轴旋转后的obb和obb2
collision = obb_collision(obb_rotated_z, obb2)
# 打印结果
if collision:
    print("发生碰撞")
else:
    print("未发生碰撞")
