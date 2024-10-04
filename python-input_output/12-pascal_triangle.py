#!/usr/bin/python3
'''
Defines a function that returns a pascal triangle.
'''


def pascal_triangle(n):
    '''
    Returns a Pascal triangle of height n in a 2D list.

    Args:
        n (int): Height of the triangle

    Return:
        triangle (List[List[int]]): Representation of a pascal triangle
    '''
    if n <= 0:
        return []

    # Initializing a 2D list with the tip of the triangle being 1
    triangle = [[1]]

    for i in range(1, n):
        # Starting each row with 1
        row = [1]

        for j in range(1, i):
            # Appending each number being the sum
            # of its adjacent in the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Ending each row with 1
        row.append(1)

        # Appending finished row to triangle
        triangle.append(row)

    return triangle
