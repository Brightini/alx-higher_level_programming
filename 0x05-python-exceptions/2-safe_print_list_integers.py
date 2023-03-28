#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers

    Args:
        my_list: (list) integers
        x: number of elements to access in @my_list

    Return:
        number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
