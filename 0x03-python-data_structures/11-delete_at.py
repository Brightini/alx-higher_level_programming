#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes a item at a specific position in a list

    Args:
        my_list: a list
        idx: index position of item

    Return:
        the modified list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            my_list[i:i+1] = []
            return my_list
