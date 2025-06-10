#!/usr/bin/python3
"""Function that returns Pascal’s triangle up to n rows."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows.

    Returns:
        List of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]

        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
