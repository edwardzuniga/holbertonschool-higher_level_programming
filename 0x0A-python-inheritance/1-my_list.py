#!/usr/bin/python3


"""a class MyList"""


class MyList(list):
    """class MyList that
    inherits from list"""
    def print_sorted(self):
        """
        that prints the list, but
        sorted (ascending sort)
        """
        print(sorted(self))
