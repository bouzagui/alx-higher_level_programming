#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(len(tuple_a), len(tuple_b)):
        tuple_a += (0, )
    for j in range(len(tuple_b), len(tuple_a)):
            tuple_b += (0, )
    if len(tuple_a) == len(tuple_b):
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
