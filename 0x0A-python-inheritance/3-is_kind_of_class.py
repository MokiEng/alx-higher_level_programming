#!/usr/bin/python3
""" defines a class and its inherited"""


def is_kind_of_class(obj, a_class):
    """ckeck an object iinstance or iherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - if obj is an instance or inherited instance of a_class.
        False - Otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
