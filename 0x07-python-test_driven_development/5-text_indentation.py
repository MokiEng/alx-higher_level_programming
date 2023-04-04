#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Prints text with two lines after each '.', '?', and ':'.

    Args:
        text(string):the text to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    b = 0
    while b < len(text) and text[b] == ' ':
        b += 1

    while b < len(text):
        print(text[b], end="")
        if text[b] == "\n" or text[b] in ".?:":
            if text[b] in ".?:":
                print("\n")
            b += 1
            while b < len(text) and text[b] == ' ':
                b += 1
            continue
        c += 1
