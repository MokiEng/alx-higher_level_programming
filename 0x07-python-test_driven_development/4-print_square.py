#!/usr/bin/python3
"""Defines a function that prints square."""


def print_square(size):
    """Print a square using # character.

    Args:
        size(int): The width/height of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
