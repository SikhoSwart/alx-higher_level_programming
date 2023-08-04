#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    mess = "matrix must be a matrix (list of lists) of integers/floats"
    mess2 = "Each row of the matrix must have the same size"
    if not matrix:
        raise TypeError(mess)
    else:
        for ele in matrix:
            if any(type(i) != int and type(i) != float for i in ele):
                raise TypeError(mess)
            if type(matrix) != list or len(ele) == 0:
                raise TypeError(mess)
        for ele in matrix:
            if len(matrix[0]) != len(ele):
                raise TypeError(mess2)
    if type(div) != int and type(div) != float or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [[round(i / div, 2) for i in ele] for ele in matrix]
    return new
