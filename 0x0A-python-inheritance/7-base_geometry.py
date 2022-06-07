#!/usr/bin/python3


"""Improve Geometry """


class BaseGeometry:
    """
    Class Base Geometry
    """
    def area(self):
        raise Exception("area() is not implemented")
    """
     Integer validator
    """
    def integer_validator(self, name, value):
        """
        the message
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
