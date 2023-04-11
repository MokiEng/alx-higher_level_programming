#!/usr/bin/python3
"""Defines a file- appending function."""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8).

    Args:
        filename(str): the file name to append.
        text(str): the string to be append to file.
    Returns:
        the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
