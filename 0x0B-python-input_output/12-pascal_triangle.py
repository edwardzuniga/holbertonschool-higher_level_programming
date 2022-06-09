#!/usr/bin/python3


'''Pascal's Triangle'''


def pascal_triangle(n):
    ''' function that returns Pascal’s triangle'''
    if n <= 0:
        return []

    mode_triangle = [[1]]

    for i in range(n - 1):
        rin = [0] + mode_triangle[-1] + [0]
        t = []
        for a in range(len(mode_triangle[-1]) + 1):
            t.append(rin[a] + rin[a + 1])
        mode_triangle.append(t)

    return mode_triangle
