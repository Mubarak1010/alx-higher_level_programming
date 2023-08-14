#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    index_1 = len(tuple_a)
    index_2 = len(tuple_b)

    if index_1 < 2:
        if index_1 == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if index_2 < 2:
        if index_2 == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
