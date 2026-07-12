
import platform,os,sys
opsystem_info = {
    'system_name': platform.system(),
    'username': os.getlogin(),
    'path': os.getcwd(),
}

#这是pygame.example里的代码

""" 

在屏幕上绘制一个立方体。

每帧我们围绕相机做一小段轨道运动，营造出立方体旋转的视觉效果。

首先我们设置了一个多彩立方体的一些点。然后我们通过一个半优化的循环来将立方体的点绘制到屏幕上。

OpenGL为我们完成了所有的繁重工作。 :]

键盘控制
-----------------
* 按 ESCAPE 键退出
* 按 f 键切换全屏模式。
"""
import math
import ctypes

import pygame

try:
    import OpenGL.GL as GL
    import OpenGL.GLU as GLU
except ImportError:
    print('PyOpenGL未安装')
    import PyOpenGL
    sys.exit()

from numpy import array, dot, eye, zeros, float32, uint32


# 我们是否想使用 新OpenGL API 还是旧的API？
# 本例演示了两者如何使用。
USE_MODERN_GL = True

# 这里有一个彩色立方体的一些简单数据
# 每个顶点的数组
CUBE_POINTS = (
    (0.5, -0.5, -0.5),
    (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5),
    (0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),
    (-0.5, 0.5, 0.5),
)

# 每个顶点的颜色数组，颜色为0-1的浮点值
# 颜色附着在顶点是为了实现颜色的渐变
CUBE_COLORS = (
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (1, 0, 1),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 1),
)

#每个面的数组
CUBE_QUAD_VERTS = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

#每条边的数组
CUBE_EDGES = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)


def translate(matrix, x=0.0, y=0.0, z=0.0):
    """
    将矩阵在x、y和z轴上平移（移动）。

    :param matrix: 要平移的矩阵。
    :param x: 在x轴上平移的方向和大小。默认为0。
    :param y: 在y轴上平移的方向和大小。默认为0。
    :param z: 在z轴上平移的方向和大小。默认为0。
    :return: 平移后的矩阵。
    """
    translation_matrix = array(
        [
            [1.0, 0.0, 0.0, x],
            [0.0, 1.0, 0.0, y],
            [0.0, 0.0, 1.0, z],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=matrix.dtype,
    ).T
    matrix[...] = dot(matrix, translation_matrix)
    return matrix


def frustum(left, right, bottom, top, znear, zfar):
    """
    从剪裁平面或相机“frustrum”体量构建透视矩阵。

    :param left: 近裁剪平面的左边位置。
    :param right: 近裁剪平面的右边位置。
    :param bottom: 近裁剪平面的底部位置。
    :param top: 近裁剪平面的上边位置。
    :param znear: 近裁剪平面的深度。
    :param zfar: 远裁剪平面的深度。

    :return: 透视矩阵。
    """
    perspective_matrix = zeros((4, 4), dtype=float32)
    perspective_matrix[0, 0] = +2.0 * znear / (right - left)
    perspective_matrix[2, 0] = (right + left) / (right - left)
    perspective_matrix[1, 1] = +2.0 * znear / (top - bottom)
    perspective_matrix[3, 1] = (top + bottom) / (top - bottom)
    perspective_matrix[2, 2] = -(zfar + znear) / (zfar - znear)
    perspective_matrix[3, 2] = -2.0 * znear * zfar / (zfar - znear)
    perspective_matrix[2, 3] = -1.0
    return perspective_matrix


def perspective(fovy, aspect, znear, zfar):
    """
    根据视野角、宽高比和深度平面构建透视矩阵。

    :param fovy: y轴的视野角度。
    :param aspect: 视口的宽高比。
    :param znear: 近裁剪面的深度。
    :param zfar: 远裁剪面的深度。

    :return: 透视矩阵。
    """
    h = math.tan(fovy / 360.0 * math.pi) * znear
    w = h * aspect
    return frustum(-w, w, -h, h, znear, zfar)


def rotate(matrix, angle, x, y, z):
    """
    绕轴旋转矩阵。

    :param matrix: 要旋转的矩阵。
    :param angle: 旋转角度。
    :param x: 绕其旋转的轴的x坐标。
    :param y: 绕其旋转的轴的y坐标。
    :param z: 绕其旋转的轴的z坐标。

    :return: 旋转后的矩阵。
    """
    angle = math.pi * angle / 180
    c, s = math.cos(angle), math.sin(angle)
    n = math.sqrt(x * x + y * y + z * z)
    x, y, z = x / n, y / n, z / n
    cx, cy, cz = (1 - c) * x, (1 - c) * y, (1 - c) * z
    rotation_matrix = array(
        [
            [cx * x + c, cy * x - z * s, cz * x + y * s, 0],
            [cx * y + z * s, cy * y + c, cz * y - x * s, 0],
            [cx * z - y * s, cy * z + x * s, cz * z + c, 0],
            [0, 0, 0, 1],
        ],
        dtype=matrix.dtype,
    ).T
    matrix[...] = dot(matrix, rotation_matrix)
    return matrix


class Rotation:
    """
    存储三个轴的旋转角度的数据类。
    """
    def __init__(self):
        self.theta = 20
        self.phi = 40
        self.psi = 25


def drawcube_old():
    """
    使用旧的OpenGL方法（3.2之前的版本）绘制立方体。
    """
    allpoints = list(zip(CUBE_POINTS, CUBE_COLORS))

    GL.glBegin(GL.GL_QUADS)
    for face in CUBE_QUAD_VERTS:
        for vert in face:
            pos, color = allpoints[vert]
            GL.glColor3fv(color)
            GL.glVertex3fv(pos)
    GL.glEnd()

    GL.glColor3f(1.0, 1.0, 1.0)
    GL.glBegin(GL.GL_LINES)
    for line in CUBE_EDGES:
        for vert in line:
            pos, color = allpoints[vert]
            GL.glVertex3fv(pos)

    GL.glEnd()


def init_gl_stuff_old():
    """
    在3.2之前的版本中初始化OpenGL。
    """
    GL.glEnable(GL.GL_DEPTH_TEST)  # 使用深度缓冲区

    # 设置相机
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GLU.gluPerspective(45.0, 640 / 480.0, 0.1, 100.0)  # 设置透视投影
    GL.glTranslatef(0.0, 0.0, -3.0)  # 后移
    GL.glRotatef(25, 1, 0, 0)  # 旋转高度


def init_gl_modern(display_size):
    """
    以OpenGL版本高于3.1的 新版OpenGL样式 初始化OpenGL。

    :param display_size: 窗口/视口的大小。
    """

    # 创建着色器
    # --------------------------------------
    vertex_code = """
    #version 150
    uniform mat4   model;
    uniform mat4   view;
    uniform mat4   projection;

    uniform vec4   colour_mul;
    uniform vec4   colour_add;

    in vec4 vertex_colour;         // 顶点颜色输入
    in vec3 vertex_position;

    out vec4   vertex_color_out;            // 顶点颜色输出
    void main()
    {
        vertex_color_out = (colour_mul * vertex_colour) + colour_add;
        gl_Position = projection * view * model * vec4(vertex_position, 1.0);
    }
    """

    fragment_code = """
    #version 150
    in vec4 vertex_color_out;  // 从顶点着色器获取的顶点颜色
    out vec4 fragColor;
    void main()
    {
        fragColor = vertex_color_out;
    }
    """

    program = GL.glCreateProgram()
    vertex = GL.glCreateShader(GL.GL_VERTEX_SHADER)
    fragment = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
    GL.glShaderSource(vertex, vertex_code)
    GL.glCompileShader(vertex)

    # 输出着色器编译器的日志信息
    log = GL.glGetShaderInfoLog(vertex)
    if isinstance(log, bytes):
        log = log.decode()
    for line in log.split("\n"):
        print(line)

    GL.glAttachShader(program, vertex)
    GL.glShaderSource(fragment, fragment_code)
    GL.glCompileShader(fragment)

    # 输出着色器编译器的日志信息
    log = GL.glGetShaderInfoLog(fragment)
    if isinstance(log, bytes):
        log = log.decode()
    for line in log.split("\n"):
        print(line)

    GL.glAttachShader(program, fragment)
    GL.glValidateProgram(program)
    GL.glLinkProgram(program)

    GL.glDetachShader(program, vertex)
    GL.glDetachShader(program, fragment)
    GL.glUseProgram(program)

    # 创建顶点缓冲区和着色器常量
    # ------------------------------------------

    # 立方体数据
    vertices = zeros(
        8, [("vertex_position", float32, 3), ("vertex_colour", float32, 4)]
    )

    vertices["vertex_position"] = [
        [1, 1, 1],
        [-1, 1, 1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
    ]

    vertices["vertex_colour"] = [
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
    ]

    filled_cube_indices = array(
        [
            0,
            1,
            2,
            0,
            2,
            3,
            0,
            3,
            4,
            0,
            4,
            5,
            0,
            5,
            6,
            0,
            6,
            1,
            1,
            6,
            7,
            1,
            7,
            2,
            7,
            4,
            3,
            7,
            3,
            2,
            4,
            7,
            6,
            4,
            6,
            5,
        ],
        dtype=uint32,
    )

    outline_cube_indices = array(
        [0, 1, 1, 2, 2, 3, 3, 0, 4, 7, 7, 6, 6, 5, 5, 4, 0, 5, 1, 6, 2, 7, 3, 4],
        dtype=uint32,
    )
    
    shader_data = {"buffer": {}, "constants": {}}
    
    GL.glBindVertexArray(GL.glGenVertexArrays(1))  # 首先要执行这个操作
    
    # 创建并绑定顶点缓冲区
    shader_data["buffer"]["vertices"] = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, shader_data["buffer"]["vertices"])
    GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL.GL_DYNAMIC_DRAW)
    
    stride = vertices.strides[0]  # 步长
    offset = ctypes.c_void_p(0)  # 偏移量
    
    loc = GL.glGetAttribLocation(program, "vertex_position")  # 获取顶点位置的属性位置
    GL.glEnableVertexAttribArray(loc)  # 启用顶点属性数组
    GL.glVertexAttribPointer(loc, 3, GL.GL_FLOAT, False, stride, offset)  # 设置顶点属性指针
    
    offset = ctypes.c_void_p(vertices.dtype["vertex_position"].itemsize)  # 更新偏移量
    
    loc = GL.glGetAttribLocation(program, "vertex_colour")  # 获取顶点颜色的属性位置
    GL.glEnableVertexAttribArray(loc)  # 启用顶点属性数组
    GL.glVertexAttribPointer(loc, 4, GL.GL_FLOAT, False, stride, offset)  # 设置顶点属性指针
    
    # 创建并绑定填充立方体的索引缓冲区
    shader_data["buffer"]["filled"] = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, shader_data["buffer"]["filled"])
    GL.glBufferData(
        GL.GL_ELEMENT_ARRAY_BUFFER,
        filled_cube_indices.nbytes,
        filled_cube_indices,
        GL.GL_STATIC_DRAW,
    )
    
    # 创建并绑定轮廓立方体的索引缓冲区
    shader_data["buffer"]["outline"] = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, shader_data["buffer"]["outline"])
    GL.glBufferData(
        GL.GL_ELEMENT_ARRAY_BUFFER,
        outline_cube_indices.nbytes,
        outline_cube_indices,
        GL.GL_STATIC_DRAW,
    )
    
    # 获取着色器中的常量位置并赋值
    shader_data["constants"]["model"] = GL.glGetUniformLocation(program, "model")
    GL.glUniformMatrix4fv(shader_data["constants"]["model"], 1, False, eye(4))
    
    shader_data["constants"]["view"] = GL.glGetUniformLocation(program, "view")
    view = translate(eye(4), z=-6)
    GL.glUniformMatrix4fv(shader_data["constants"]["view"], 1, False, view)
    
    shader_data["constants"]["projection"] = GL.glGetUniformLocation(
        program, "projection"
    )
    GL.glUniformMatrix4fv(shader_data["constants"]["projection"], 1, False, eye(4))
    
    # 颜色乘法，用于生成最终输出颜色
    shader_data["constants"]["colour_mul"] = GL.glGetUniformLocation(
        program, "colour_mul"
    )
    GL.glUniform4f(shader_data["constants"]["colour_mul"], 1, 1, 1, 1)
    
    # 颜色加法，用于生成最终输出颜色
    shader_data["constants"]["colour_add"] = GL.glGetUniformLocation(
        program, "colour_add"
    )
    GL.glUniform4f(shader_data["constants"]["colour_add"], 0, 0, 0, 0)
    
    # 设置OpenGL绘图相关的参数
    GL.glClearColor(0, 0, 0, 0)  # 清除颜色
    GL.glPolygonOffset(1, 1)  # 多边形偏移
    GL.glEnable(GL.GL_LINE_SMOOTH)  # 启用线平滑
    GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)  # 混合函数
    GL.glDepthFunc(GL.GL_LESS)  # 深度测试函数
    GL.glHint(GL.GL_LINE_SMOOTH_HINT, GL.GL_NICEST)  # 线平滑提示
    GL.glLineWidth(1.0)  # 线宽度
    
    # 设置投影矩阵
    projection = perspective(45.0, display_size[0] / float(display_size[1]), 2.0, 100.0)
    GL.glUniformMatrix4fv(shader_data["constants"]["projection"], 1, False, projection)
    
    return shader_data, filled_cube_indices, outline_cube_indices



def draw_cube_modern(shader_data, filled_cube_indices, outline_cube_indices, rotation):
    """
    绘制一个在OpenGL的新版样式下的立方体，适用于3.1版本及以上的OpenGL。

    :param shader_data: 用于绘制立方体的顶点和像素着色器数据。
    :param filled_cube_indices: 绘制'填充'立方体所需的索引。
    :param outline_cube_indices: 绘制'轮廓'立方体所需的索引。
    :param rotation: 当前需要应用的旋转角度。
    """

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    # 绘制填充立方体
    GL.glDisable(GL.GL_BLEND)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_POLYGON_OFFSET_FILL)
    GL.glUniform4f(shader_data["constants"]["colour_mul"], 1, 1, 1, 1)
    GL.glUniform4f(shader_data["constants"]["colour_add"], 0, 0, 0, 0.0)
    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, shader_data["buffer"]["filled"])
    GL.glDrawElements(
        GL.GL_TRIANGLES, len(filled_cube_indices), GL.GL_UNSIGNED_INT, None
    )

    # 绘制轮廓立方体
    GL.glDisable(GL.GL_POLYGON_OFFSET_FILL)
    GL.glEnable(GL.GL_BLEND)
    GL.glUniform4f(shader_data["constants"]["colour_mul"], 0, 0, 0, 0.0)
    GL.glUniform4f(shader_data["constants"]["colour_add"], 1, 1, 1, 1.0)
    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, shader_data["buffer"]["outline"])
    GL.glDrawElements(GL.GL_LINES, len(outline_cube_indices), GL.GL_UNSIGNED_INT, None)

    # 旋转立方体
    # rotation.theta += 1.0  # 角度
    rotation.phi += 1.0  # 角度
    # rotation.psi += 1.0  # 角度
    model = eye(4, dtype=float32)
    # rotate(model, rotation.theta, 0, 0, 1)
    rotate(model, rotation.phi, 0, 1, 0)
    rotate(model, rotation.psi, 1, 0, 0)
    GL.glUniformMatrix4fv(shader_data["constants"]["model"], 1, False, model)


def main():
    """运行演示"""
    
    # 初始化 pygame 并设置一个 OpenGL 显示
    pygame.init()
    def show_text(screen,text,color=(0,0,0),pos=(0,0),size=30):
        if opsystem_info['system_name'] == 'Windows':
            screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)
        else:
            screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)
    gl_version = (3, 0)  # OpenGL 版本号（主要版本号，次要版本号）
    if USE_MODERN_GL:
        gl_version = (3, 2)  # OpenGL 版本号（主要版本号，次要版本号）
    
        # 通过设置这些属性，我们可以选择使用哪个 OpenGL Profile，
        # 版本大于 3.2 的 Profile 使用了不同的渲染路径
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, gl_version[0])
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, gl_version[1])
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
        )
    
    fullscreen = False  # 初始为窗口模式
    
    display_size = (640, 480)
    pygame.display.set_mode(
        display_size, pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE
    )
    
    if USE_MODERN_GL:
        gpu, f_indices, o_indices = init_gl_modern(display_size)
        rotation = Rotation()
    else:
        init_gl_stuff_old()
    
    going = True
    while going:
        # 检测退出事件
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                going = False
    
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                if not fullscreen:
                    print("切换到全屏模式")
                    pygame.display.set_mode(
                        (640, 480), pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN
                    )
                else:
                    print("切换到窗口模式")
                    pygame.display.set_mode(
                        (640, 480), pygame.OPENGL | pygame.DOUBLEBUF
                    )
                fullscreen = not fullscreen
                if gl_version[0] >= 4 or (gl_version[0] == 3 and gl_version[1] >= 2):
                    gpu, f_indices, o_indices = init_gl_modern(display_size)
                    rotation = Rotation()
                else:
                    init_gl_stuff_old()
    
        if USE_MODERN_GL:
            draw_cube_modern(gpu, f_indices, o_indices, rotation)
        else:
            # 清空屏幕并移动相机
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
            # 将相机围绕 Y 轴旋转 1 度
            GL.glRotatef(1, 0, 1, 0)
            drawcube_old()
        #show_text(pygame.display.set_mode((640, 480), pygame.OPENGL | pygame.DOUBLEBUF),f'FPS: {round(pygame.time.Clock().get_fps())}',pos=(11,11),color=(255,255,255))

        pygame.display.flip()
        pygame.time.wait(10)
    
    pygame.quit()
if __name__ == "__main__":
    main()
