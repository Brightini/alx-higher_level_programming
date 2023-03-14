#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    prints all integers of a list

    Args:
        my_list: list of integers
    """
    for item in my_list:
        print("{:d}".format(item))
