#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for row in range(n):
        line = []
        for col in range(row + 1):
            if col == 0 or col == row:
                line.append(1)
            elif row > 0 and col > 0:
                line.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        triangle.append(line)
    return triangle
