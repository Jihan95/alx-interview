#!/usr/bin/python3
"""
rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    function to rotate 2d matrix
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
