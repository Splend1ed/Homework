def to_power(x, exp: int):
    if exp == 0:
        return 1
    return x*to_power(x, exp-1)


print(to_power(2, -1))


"""
Returns  x ^ exp

>>> to_power(2, 3) == 8
True

>>> to_power(3.5, 2) == 12.25
True

>>> to_power(2, -1)
ValueError: This function works only with exp > 0.
"""
