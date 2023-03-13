#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replaces an element at an index position

    Args:
        my_list: list of integers
        idx: position of element to be replaced
        element: new element

    Return:
        original list if idx is negative or out of range
        else, the new list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
