#!/usr/bin/python3
def element_at(my_list, idx):
    """
    retrieves an element from a list

    Args:
        my_list: list of integer
        idx: index of element to be retrieved

    Return:
        None if idx is negative or out of range
        else, the element at idx
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
