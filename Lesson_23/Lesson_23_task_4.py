def reverse(input_str: str) -> str:
    if input_str == "":
        return input_str
    return reverse(input_str[1:]) + input_str[0]


print(reverse("ierdnA"))


"""
Function returns reversed input string
>>> reverse("hello") == "olleh"
True
>>> reverse("o") == "o"
True
"""