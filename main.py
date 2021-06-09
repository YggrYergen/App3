import sys
import numpy as np


def paths(maze):
    return np.argwhere(maze == 0)


if __name__ == "__main__":
    maze = np.loadtxt(sys.argv[1], dtype='i')
    print(paths(maze))
