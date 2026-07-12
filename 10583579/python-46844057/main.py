import pygame
import numpy as np
import heapq
import warnings
from numba import jit, prange
from numba.core.errors import NumbaWarning

# 屏蔽warning
warnings.filterwarnings('ignore', category=NumbaWarning)

# Define the 8 vertices of the cube
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# Define the 6 faces of the cube, each face is a list of vertices
faces = [(0, 1, 2, 3),
         (1, 5, 6, 2),
         (5, 4, 7, 6),
         (4, 0, 3, 7),
         (0, 4, 5, 1),
         (3, 2, 6, 7)]

# Load the texture
texture = pygame.image.load('img.png')
texture_np = pygame.surfarray.array3d(texture)

# Define the light source
light = np.array([0, 0, 3])

def project(points, screen_width, screen_height, fov, viewer_distance):
    factor = fov / (viewer_distance + points[2])
    x = points[0] * factor + screen_width / 2
    y = -points[1] * factor + screen_height / 2
    return np.array([x, y, points[2]])  # Return z coordinate

def rotate(points, angle):
    rot_matrix_y = np.array([[np.cos(angle), 0, np.sin(angle)],
                             [0, 1, 0],
                             [-np.sin(angle), 0, np.cos(angle)]])
    return np.dot(points, rot_matrix_y)

@jit(nopython=True)
def point_in_polygon(x, y, polygon):
    # This is a simplified version of the ray casting algorithm
    # It assumes that the polygon is convex and the point is within the bounding box of the polygon
    inside = False
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if y > min(y1, y2):
            if y <= max(y1, y2):
                if x <= max(x1, x2):
                    if y1 != y2:
                        xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if x1 == x2 or x <= xinters:
                        inside = not inside
    return inside

@jit(nopython=True)
def rasterize_polygon(screen_np, points, texture_np, min_x, max_x, min_y, max_y, intensity):
    # Set the color of the pixels inside the polygon
    for i in prange(min_x, max_x):
        for j in prange(min_y, max_y):
            if point_in_polygon(i, j, points):
                # Map the pixel to the texture
                u = (i - min_x) / (max_x - min_x)
                v = (j - min_y) / (max_y - min_y)
                tex_x = int(u * texture_np.shape[0])
                tex_y = int(v * texture_np.shape[1])
                color = texture_np[tex_x, tex_y]
                screen_np[i, j] = np.clip(color * intensity, 0, 255)

def calculate_intensity(face, vertices, light):
    # Calculate the normal of the face
    normal = np.cross(vertices[face[1]] - vertices[face[0]], vertices[face[2]] - vertices[face[0]])
    normal = normal / np.linalg.norm(normal)  # Normalize the normal

    # Calculate the vector from the face to the light
    face_center = np.mean([vertices[i] for i in face], axis=0)
    light_vector = light - face_center
    light_vector = light_vector / np.linalg.norm(light_vector)  # Normalize the light vector

    # Calculate the intensity of the light
    intensity = np.dot(normal, light_vector)
    if intensity < 0:  # The face is backfacing
        intensity = 0

    return intensity

def draw_cube(screen, vertices, faces, texture_np, angle, screen_width, screen_height, fov, viewer_distance):
    # Rotate vertices
    rotated_vertices = [rotate((x, y, z), angle) for x, y, z in vertices]

    # Calculate depth and intensity of each face
    depths = []
    intensities = []
    for face in faces:
        # Calculate depth
        depths.append(sum(rotated_vertices[i][2] for i in face) / 4)

        # Calculate intensity
        intensities.append(calculate_intensity(face, rotated_vertices, light))

    # Project vertices
    projected_vertices = [project(v, screen_width, screen_height, fov, viewer_distance) for v in rotated_vertices]

    # Create a priority queue for the faces
    face_queue = []

    # Update the priority queue
    for face, depth, intensity in zip(faces, depths, intensities):
        heapq.heappush(face_queue, (-depth, (face, intensity)))  # Use negative depth because heapq is a min-heap

    # Draw each face
    while face_queue:
        _, (face, intensity) = heapq.heappop(face_queue)
        points = [projected_vertices[i][:2] for i in face]  # Only use x and y coordinates for drawing
        min_x = int(min(point[0] for point in points))
        max_x = int(max(point[0] for point in points))
        min_y = int(min(point[1] for point in points))
        max_y = int(max(point[1] for point in points))
        screen_np = pygame.surfarray.array3d(screen)
        rasterize_polygon(screen_np, points, texture_np, min_x, max_x, min_y, max_y, intensity)
        pygame.surfarray.blit_array(screen, screen_np)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))
        draw_cube(screen, vertices, faces, texture_np, angle, 800, 600, 800, 10)  # Increase viewer_distance to 10
        pygame.display.flip()
        clock.tick(60)
        angle += 0.05

if __name__ == "__main__":
    main()