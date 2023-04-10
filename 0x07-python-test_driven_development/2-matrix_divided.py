#!/usr/bin/python3
"""matrix module"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Args:
        matrix: (list) a matrix of integers or float
        div: (int/float) a divisor

    Raises:
        div:
            TypeError: if @div is not an int or float
            ZeroDivisionError: if @div is of value 0
        matrix:
            TypeError: if @matrix is not a list of list of integers or floats
                       if each row in @matrix is not of the same size

    Return:
        new matrix
    """

    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif div == float('inf') or div == float('-inf'):
        raise OverflowError("float overflow")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

        list_len = len(matrix[0])
        if list_len != len(item):
            raise TypeError("Each row of the matrix must have the same size")

        for num in item:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    new_matrix = [[round((num / div), 2) for num in row] for row in matrix]
    return (new_matrix)
