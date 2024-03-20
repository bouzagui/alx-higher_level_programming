#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        a = list(map(lambda i: i ** 2, i))
        square_matrix.append(a)
    return square_matrix
