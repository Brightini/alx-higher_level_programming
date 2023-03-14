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

    integers = [x for x in my_list if isinstance(x, int)]
    for i in range(len(integers)-1, -1, -1):
        print("{:d}".format(integers[i]))
