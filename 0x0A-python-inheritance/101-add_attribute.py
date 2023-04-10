#!/usr/bin/python3
"""Defines  a function that adds a new attribute to an object if it’s possible.
"""


def add_attribute(obj, new_att, value):
    """Add a new attribute to an object if it's possible.
    Args:
        obj(any): The object to add an attribute to.
        new_att(str): The name of the attribute to add to obj.
        value(any): The value of new_att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, new_att, value)
