#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number."""
    i = number - (10 * (number / 10))
    print("{}".format(i, end=""))
    return (i)
