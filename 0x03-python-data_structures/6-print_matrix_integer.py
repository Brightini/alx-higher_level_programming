#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    prints a matrix of integers

    Args:
        matrix: a list of lists of integers
    """
    # Get the number of rows and columns
    num_rows = len(matrix)
    num_col = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_col):
            print("{:d}".format(matrix[i][j]), end="")
            if j < num_col - 1:
                print(" ", end="")
        print()
