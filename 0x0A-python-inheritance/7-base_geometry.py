#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """"Represents BaseGeometry."""

    def area(self):
        '''Not implemented.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer.
        Args:
            name(str): The name of the parameter.
            value(int):The parameter to validete.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
