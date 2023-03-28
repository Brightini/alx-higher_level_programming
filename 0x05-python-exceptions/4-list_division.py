#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element of 2 lists and stores result in a new list.
    If an error is thrown, result at that index is equated to zero

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of new list

    Return:
        new list
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
