def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func):
        def wrap(name):
            if type(name) == type_:
                if len(name) <= max_length:
                    for items in contains:
                        if items in name:
                            return func(name)
                        else:
                            print(f'Your name must contain such characters {contains}')
                else:
                    print('Your name must be no more than 15 characters!')
                    return False
            else:
                print('Write only letters!')
        return wrap
    return wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'





