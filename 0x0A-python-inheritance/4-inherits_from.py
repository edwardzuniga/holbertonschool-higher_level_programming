#!/usr/bin/python3


"""unction that returns True or False"""


def inherits_from(obj, a_class):
    """
     Method returns True if is inherited
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
