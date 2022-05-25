#!/usr/bin/python3
"""defines a Square Class"""


class Square:
    """A class Square that defines a square by: 
    based on 1-square.py"""

    def __init__(self, size=0):
        """Start"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
