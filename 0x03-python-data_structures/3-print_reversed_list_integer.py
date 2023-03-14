#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints all integers of a list in reverse order

    Args:
        my_list: list of integers
    """
    if my_list is None:
        return
    idx = len(my_list) - 1
    for item in range(idx, -1, -1):
        if type(my_list[item]) != int:
            return
        else:
            print("{:d}".format(my_list[item]))
