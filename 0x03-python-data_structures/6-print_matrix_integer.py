#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for number in mat:
            if mat[len(mat) - 1] == number:
                print("{:d}".format(number), end='')
                print()
            else:
                print("{:d}".format(number), end=' ')



def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for element in mat:
            print("{:d}".format(element), end="" if mat[len(mat) - 1] == element else " ")
        print()
