from A import Maze
maze = Maze()
maze.generate_matrix_dfs()
maps = []
for i in maze.print_matrix():
    maps.append(list(i))
print(maps)