#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list

    Args:
        my_list: list of integers
        search: element to be replaced
        replaces: new value to replace with

    Return:
        new list of replaced items
    """
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
