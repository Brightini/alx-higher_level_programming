#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    square value of all integers of a matrix

    Args:
        matrix: a 2D array of integers

    Return: squared matrix
    """
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    return new_matrix
