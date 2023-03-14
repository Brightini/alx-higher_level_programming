#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints all integers of a list in reverse order

    Args:
        my_list: list of integers
    """
    idx = len(my_list) - 1
    if my_list is None or idx == 0:
        return
    for item in range(idx, -1, -1):
        if not isinstance(my_list[item], int):
            continue
        print("{:d}".format(my_list[item]))
