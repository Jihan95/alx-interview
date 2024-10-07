#!/usr/bin/python3
"""
Module that contain island perimeter function
"""


def island_perimeter(grid):
    """
    Function to calculate the island perimeter

    Args:
    grid (list of lists)

    Return:
    the island perimeter
    """
    perimeter = 0
    if type(grid) is not list or type(grid[0]) is not list:
        return perimeter
    w = len(grid)
    h = len(grid[0])
    for i in range(w):
        for j in range(h):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
