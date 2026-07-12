import pygame
import numpy as np
import matplotlib.path as mplPath
import heapq

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

# Create a priority queue for the faces
face_queue = []

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

def rasterize_polygon(screen, points, texture):
    # Create a Path object from the points
    path = mplPath.Path(points)

    # Calculate the bounding box of the polygon
    min_x = int(min(point[0] for point in points))
    max_x = int(max(point[0] for point in points))
    min_y = int(min(point[1] for point in points))
    max_y = int(max(point[1] for point in points))

    # Create a 2D grid of points within the bounding box
    y, x = np.mgrid[min_y:max_y, min_x:max_x]

    # Check each point in the grid
    inside = path.contains_points(np.vstack((x.ravel(), y.ravel())).T)

    # Reshape the result to match the shape of the grid
    inside = inside.reshape(x.shape)

    # Set the color of the pixels inside the polygon
    for i in range(inside.shape[1]):
        for j in range(inside.shape[0]):
            if inside[j, i]:
                # Map the pixel to the texture
                u = i / inside.shape[1]
                v = j / inside.shape[0]
                tex_x = int(u * texture.get_width())
                tex_y = int(v * texture.get_height())
                color = texture.get_at((tex_x, tex_y))
                screen.set_at((i + min_x, j + min_y), color)

def draw_cube(screen, vertices, faces, texture, angle, screen_width, screen_height, fov, viewer_distance):
    # Rotate and project vertices
    projected_vertices = []
    for x, y, z in vertices:
        x, y, z = rotate((x, y, z), angle)
        projected_vertices.append(project((x, y, z), screen_width, screen_height, fov, viewer_distance))

    # Calculate depth of each face
    depths = []
    for face in faces:
        depths.append(sum(projected_vertices[i][2] for i in face) / 4)

    # Update the priority queue
    for face, depth in zip(faces, depths):
        heapq.heappush(face_queue, (-depth, face))  # Use negative depth because heapq is a min-heap

    # Draw each face
    while face_queue:
        _, face = heapq.heappop(face_queue)
        points = [projected_vertices[i][:2] for i in face]  # Only use x and y coordinates for drawing
        rasterize_polygon(screen, points, texture)

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
        draw_cube(screen, vertices, faces, texture, angle, 800, 600, 800, 10)  # Increase viewer_distance to 10
        pygame.display.flip()
        clock.tick(60)
        angle += 0.01

if __name__ == "__main__":
    main()