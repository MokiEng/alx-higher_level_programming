#!/usr/bin/python3
"""Defines a a function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a specific string.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """

    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
