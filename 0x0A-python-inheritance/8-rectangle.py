#!/usr/bin/python3
"""Defines Rectangle class  that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using parent class."""

    def __init__(self, width, height):
        """Initialize a rectangle
        Args:
            width(int): The width of the new Rectangle.
            height(int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
