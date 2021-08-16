from typing import Optional


def mult(a: int, n: int) -> int:
    if n == 1:
        return a
    elif n == 0:
        return 0
    else:
        return a + mult(a, n-1)


print(mult(2, 4))

"""
This function works only with positive integers

>>> mult(2, 4) == 8
True

>>> mult(2, 0) == 0
True

>>> mult(2, -4)
ValueError("This function works only with postive integers")
"""