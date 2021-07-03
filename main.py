import numpy as np
import sys
from a import findFirst, findLast

# Check if cell (x, y) is valid or not
def is_valid_cell(x, y, N):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    return True

def find_paths_util(maze, source, destination, visited, path, paths):
  """Find paths using Breadth First Search algorith """
  # Done if destination is found
  if source == destination:
    paths.append(path[:])  # append copy of current path
    return

  # mark current cell as visited
  N = len(maze)
  x, y = source
  visited[x][y] = 1

  # if current cell is a valid and open cell, 
  if is_valid_cell(x, y, N) and maze[x][y]:
    # Using Breadth First Search on path extension in all direction

    # go right (x, y) --> (x + 1, y)
    if x + 1 < N and (not (visited[x + 1][y] != 0)):
    # if x + 1 < N :
      # print("1-visited[x + 1][y] : ", visited[x + 1][y], "if1 x :", x, "if1 y :", y)  
      path.append((x + 1, y))
      find_paths_util(maze,(x + 1, y), destination, visited, path, paths)
      path.pop()

    # go left (x, y) --> (x - 1, y)
    if x - 1 >= 0 and (not (visited[x - 1][y] != 0)):
      print("2-visited[x - 1][y] : ",  visited[x - 1][y], "if1 x :", x, "if1 y :", y)  
      path.append((x - 1, y))
      find_paths_util(maze, (x - 1, y), destination, visited, path, paths)
      path.pop()

    # go up (x, y) --> (x, y + 1)
    if y + 1 < N and (not (visited[x][y + 1] != 0)):
      print("3-visited[x][y + 1] : ", visited[x][y + 1], "if1 x :", x, "if1 y :", y)  
      path.append((x, y + 1))
      find_paths_util(maze, (x, y + 1), destination, visited, path, paths)
      path.pop()

    # go down (x, y) --> (x, y - 1)
    if y - 1 >= 0 and (not (visited[x][y - 1] != 0)):
      print("4-visited[x][y - 1] : ", visited[x][y - 1], "if1 x :", x, "if1 y :", y)  
      path.append((x, y - 1))
      find_paths_util(maze, (x, y - 1), destination, visited, path, paths)
      path.pop()

    # Unmark current cell as visited
  visited[x][y] = 0

  return paths

def find_paths(maze, source, destination):
  """ Sets up and searches for paths"""
  N = len(maze) # size of Maze is N x N

  # 2D matrix to keep track of cells involved in current path
  visited = [[0]*N for _ in range(N)]

  path = [source]
  paths = []
  paths = find_paths_util(maze, source, destination, visited, path, paths)

  return paths

  # Test Maze
matriz = [
  [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 , 1],
  [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1 , 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0 , 0]
]

N = len(matriz)

maze = np.array(matriz)
# print(matriz)

maze[maze == 1] = 2
maze[maze == 0] = 1
maze[maze == 2] = 0
print(maze)
# Start point and destination
source = (0, 0)  # top left corner
destination = (N-1, N-1)  # bottom right corner

# Find all paths
paths = find_paths(maze, source, destination)

print("Paths with '->' separator between maze cell locations")
for path in paths:
  print(*path, sep = ' -> ')
