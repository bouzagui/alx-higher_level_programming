#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, mul, div, sub
    a = 10
    b = 5
    result1 = mul(a, b)
    result2 = add(a, b)
    result3 = sub(a, b)
    result4 = div(a, b)

    print("{} + {} = {}".format(a, b, result2))
    print("{} - {} = {}".format(a, b, result3))
    print("{} * {} = {}".format(a, b, result1))
    print("{} / {} = {}".format(a, b, result4))
