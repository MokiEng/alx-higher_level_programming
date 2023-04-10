#!/usr/bin/python3
"""An inherited class function"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited from class

    Args:
        obj(any):the object to be checked
        a_class(type):the class to match the type of a class
    Returns:
        True -  if an object is an instance of a_class.
        False - Otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
