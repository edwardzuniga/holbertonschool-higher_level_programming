#!/usr/bin/python3


"""Full rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle clasee herencia from BaseGeometry
    """
    def __init__(self, width, height):
        """Inicialitation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
