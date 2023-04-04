#!/usr/bin/python3
"""  A class with its name locked class."""


class LockedClass:
    """
    prevents the user from instantiating  new instance attribute  first_name.
    """

    __slots__ = ["first_name"]
