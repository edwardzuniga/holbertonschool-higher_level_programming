#!/usr/bin/python3
""" Module for Rectangle class. """


class Rectangle:
    """
    Representation of a Rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        if not self.__width or not self.__height:
            return ""
        w = self.width
        h = self.height
        return ((str(self.print_symbol) * w + '\n') * h)[:-1]

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
