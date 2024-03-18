#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < len(tuple_b):
        tuple_a += (0,) * (len(tuple_b) - len(tuple_a))
    elif len(tuple_a) > len(tuple_b):
        tuple_b += (0,) * (len(tuple_a) - len(tuple_b))
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
