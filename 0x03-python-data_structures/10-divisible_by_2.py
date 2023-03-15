#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    finds all multiples of 2 in a list

    Args:
        my_list: a list of integers

    Return:
        new list
    """
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
