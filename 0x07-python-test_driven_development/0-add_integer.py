#!/usr/bin/python3
""" Defines addition function of two integers."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    Float arguments are typecasted to ints before adding is performed.

    Raises:
        TypeError:If either of them is non-int and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
