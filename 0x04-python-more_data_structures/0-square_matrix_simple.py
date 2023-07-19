#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = matrix.copy()
    for row in range(len(matrix)):
        sqr[row] = list(map(lambda x: x**2, matrix[row]))
    return sqr
