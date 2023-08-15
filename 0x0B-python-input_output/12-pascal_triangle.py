#!/usr/bin/python3
"""returns a list of lists of integers representing Pascal’s triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s,
    triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    p_tri = [[1]]
    for i in range(n - 1):
        p_tri.append([j + n for j, n in zip(p_tri[-1] + [0], [0] + p_tri[-1])])
    return (p_tri)
