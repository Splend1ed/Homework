def sum_of_digits(digit_string: str) -> int:
    if digit_string.isdigit():
        if len(digit_string) > 1:
            return eval(f"{digit_string[0]} + {sum_of_digits(digit_string[1:])}")
        else:
            return eval(f"{digit_string}")
    else:
        raise ValueError("input string must be digit string")


assert sum_of_digits('246456') == 27


"""
>>> sum_of_digits('26') == 8
True

>>> sum_of_digits('test')
ValueError("input string must be digit string")
"""