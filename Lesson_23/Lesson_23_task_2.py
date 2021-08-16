from typing import Optional


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    revers_index = -index - 1
    looking_list = list(looking_str)
    if looking_list[index] == looking_list[revers_index]:
        return True
    else:
        try:
            is_palindrome(looking_str, index + 1)
        except IndexError:
            return False
    return False


print(is_palindrome('WsasW'))


"""
Checks if input string is Palindrome
>>> is_palindrome('mom')
True

>>> is_palindrome('sassas')
True

>>> is_palindrome('o')
True
"""