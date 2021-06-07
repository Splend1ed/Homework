def our_func(func):
    return func


def func1():
    def func2():
        print('Hi')
    return func2()


our_func(func1())
