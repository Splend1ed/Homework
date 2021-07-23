def logger(func):
    def wrapper(*args, **kwargs):
        func(*args, *kwargs)
        print(f'{func.__name__}{args}')
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# add(4, 5)
# square_all(4, 5)
