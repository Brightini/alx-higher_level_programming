#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds 2 tuples
    If a tuple is smaller than 2, the value 0 is used for each missing integer
    If a tuple is bigger than 2, only the first 2 integers are used

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Return:
        new tuple
    """
    # Use list comprehension to ensure both tuples have at least two items
    list_a = [tuple_a[i] if i < len(tuple_a) else 0 for i in range(2)]
    list_b = [tuple_b[i] if i < len(tuple_b) else 0 for i in range(2)]

    sum_0 = list_a[0] + list_b[0]
    sum_1 = list_a[1] + list_b[1]
    new_tuple = (sum_0, sum_1)

    return (new_tuple)
