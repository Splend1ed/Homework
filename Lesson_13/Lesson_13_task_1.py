def veriable_counter(func):
    print(func.__code__.co_nlocals)


def test():
    veriable_1 = 1
    veriable_2 = 2
    veriable_3 = 3
    veriable_4 = 4
    veriable_5 = 5


veriable_counter(test)
