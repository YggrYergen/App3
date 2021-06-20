import sys
import numpy as np
from aux import findFirst, findLast


def positions(maze):
    return np.argwhere(maze == 0)


def paths(maze):

    return findFirst(positions(maze))


if __name__ == "__main__":
    maze = np.loadtxt(sys.argv[1], dtype='i')
    print(paths(maze))
