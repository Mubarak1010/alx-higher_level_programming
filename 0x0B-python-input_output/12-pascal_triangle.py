#!/usr/bin/python3
"""Module."""


def pascal_triangle(n):
    """ list of lists of integers representing the Pascal’s
    triangle of n

    Args:
    n (int): number
    """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])

            tmp.append(1)

            triangles.append(tmp)
            return triangles
