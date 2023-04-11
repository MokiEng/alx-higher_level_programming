#!/usr/bin/python3
'''Defines a Pascal's Triangle function.'''


def pascal_triangle(n):
    """a Pascal's Triangle size of n.
     that returns a list of lists of integers representing the
        Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    pascal_ triangle = [[1]]
    while len(pascal_ triangle) != n:
        new_tri = pascal_ triangle[-1]
        temp = [1]
        for i in range(len(new_tri) - 1):
            temp.append(new_tri[i] + new_tri[i + 1])
        temp.append(1)
        pascal_ triangle.append(temp)
    return pascal_ triangle
