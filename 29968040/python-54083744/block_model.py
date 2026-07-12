import numpy as np


class BlockModel:  # 存储方块的 3d 模型（不包括纹理图片）
    def __init__(self, filename):
        """
        https://en.wikipedia.org/wiki/Wavefront_.obj_file#Vertex_normal_indices
        """
        self.vertices = []
        self.uv_vertices = []
        self.uv_indices = []
        self.indices = []

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([[x], [y], [z], [1]]))
                elif line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    self.uv_vertices.append([u, v])
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    if len(facet) == 4:
                        self.indices.append([int(d[0])-1 for d in (facet[0], facet[1], facet[2])])
                        self.uv_indices.append([int(d[1])-1 for d in (facet[0], facet[1], facet[2])])
                        self.indices.append([int(d[0]) - 1 for d in (facet[0], facet[2], facet[3])])
                        self.uv_indices.append([int(d[1]) - 1 for d in (facet[0], facet[2], facet[3])])

        self.vertices = np.array(self.vertices)
        self.uv_vertices = np.array(self.uv_vertices)
        self.indices = np.array(self.indices)
        self.uv_indices = np.array(self.uv_indices)
