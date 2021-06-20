import sys
import numpy as np
from aux import findFirst, findLast


def positions(maze):
    return np.argwhere(maze == 0)


maze = np.loadtxt(sys.argv[1], dtype='i')
m = []
start = findFirst(positions(maze))[0], findFirst(positions(maze))[1]
end = findLast(positions(maze))[0], findLast(positions(maze))[1]


for i in range(len(maze)):
    m.append([])
    for j in range(len(maze[i])):
        m[-1].append(0)
i, j = start
m[i][j] = 1


def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i > 0 and m[i-1][j] == 0 and maze[i-1][j] == 0:
                    m[i-1][j] = k + 1
                if j > 0 and m[i][j-1] == 0 and maze[i][j-1] == 0:
                    m[i][j-1] = k + 1
                if i < len(m)-1 and m[i+1][j] == 0 and maze[i+1][j] == 0:
                    m[i+1][j] = k + 1
                if j < len(m[i])-1 and m[i][j+1] == 0 and maze[i][j+1] == 0:
                    m[i][j+1] = k + 1


k = 0
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)


i, j = end
k = m[i][j]
the_path = [(i, j)]
while k > 1:
    if i > 0 and m[i - 1][j] == k-1:
        i, j = i-1, j
        the_path.insert(0, (i, j))
        k -= 1
    elif j > 0 and m[i][j - 1] == k-1:
        i, j = i, j-1
        the_path.insert(0, (i, j))
        k -= 1
    elif i < len(m) - 1 and m[i + 1][j] == k-1:
        i, j = i+1, j
        the_path.insert(0, (i, j))
        k -= 1
    elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
        i, j = i, j+1
        the_path.insert(0, (i, j))
        k -= 1

print(the_path)
