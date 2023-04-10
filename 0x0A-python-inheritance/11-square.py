#!/usr/bin/python3
""" A Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size(int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
