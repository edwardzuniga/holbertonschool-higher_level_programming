#!/usr/bin/python3

"""Print square"""

def print_square(size):
    """
    prints a square with the character #
    """
    if isinstance (size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
