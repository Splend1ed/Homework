class TypeDecorators:
    @staticmethod
    def to_int(func):
        def conversation(*args, **kwargs):
            try:
                return func(int(*args, **kwargs))
            except (TypeError, ValueError):
                return 'You cant do this'
        return conversation

    @staticmethod
    def to_str(func):
        def conversation(*args, **kwargs):
            try:
                return func(str(*args, **kwargs))
            except (TypeError, ValueError):
                return 'You cant do this'
        return conversation

    @staticmethod
    def to_bool(func):
        def conversation(*args, **kwargs):
            if args == 'True' or 'False':
                return func(bool(*args, **kwargs))
            else:
                return 'You cant do this'
        return conversation

    @staticmethod
    def to_float(func):
        def conversation(*args, **kwargs):
            try:
                return func(float(*args, **kwargs))
            except (TypeError, ValueError):
                return 'You cant do this'
        return conversation


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
