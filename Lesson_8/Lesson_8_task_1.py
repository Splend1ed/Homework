def oops():
    a = [0, 1, 2]
    a[3]


def error_check():
    try:
        oops()
    except IndexError:
        print('(IndexError), your list is shorter than the index you specified')


error_check()