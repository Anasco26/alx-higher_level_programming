#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
        Find the square of each element
        of a matrix
    """
    return([list(map(lambda x: x**2, row)) for row in matrix])
