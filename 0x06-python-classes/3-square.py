#!/usr/bin/python3
"""Area of a square"""


class Square:
    """that defines a square by: (based on 2-square.py)"""

    def __init__(self, size=0):
        """Start"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate rea of a square"""
        return (self.__size) ** 2
