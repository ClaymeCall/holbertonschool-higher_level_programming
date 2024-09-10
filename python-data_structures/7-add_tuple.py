#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    # Padding eventual missing elements with zeros and storing the results
    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]

    result = (a1 + b1, a2 + b2)
    return (result)