def stop_words(words: list):
    def wrapper(func):
        def wrap(*args):
            result = func(*args)
            for i in words:
                result = result.replace(i, '*')
            return result
        return wrap
    return wrapper


@stop_words(['coca-cola', 'Mercedes'])
def create_slogan(name: str) -> str:
    return f"{name} drinks coca-cola in his brand new Mercedes!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

print(create_slogan('Steve'))
