#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    prints a dictionary by ordered keys

    Args:
        a_dictionary: a key-value pair of items
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
