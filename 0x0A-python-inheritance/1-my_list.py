#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """sorts a list of integers in ascending order"""
        if not all(isinstance(i, int) for i in self):
            raise TypeError("must be a list of integers")
        print(sorted(self))
