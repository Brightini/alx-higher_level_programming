#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints all integers of a list in reverse order

    Args:
        my_list: list of integers
    """
    idx = len(my_list)
    for item in range(idx, 0, -1):
        print("{}".format(item))
