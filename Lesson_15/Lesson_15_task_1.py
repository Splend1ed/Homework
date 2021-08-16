class Link:

    @classmethod
    def validate(cls, email: str):
        email_tuple = email.partition('@')
        prefix = email_tuple[0]
        domain = email_tuple[2]
        unicode_symbols = [chr(i) for i in range(0x020, 0x002F + 1)]
        unicode_symbols.pop(14)
        if domain == '' or prefix == '':
            print('Incorrect e-mail address!')
        else:
            if domain != 'gmail.com':
                print('Domain must be only "@gmail.com"')
            else:
                for symbol in unicode_symbols:
                    if symbol in prefix:
                        print(f"Don't use this symbols ({symbol})!")
                else:
                    try:
                        if prefix[prefix.index('\u002E') + 1] == '\u002E':
                            print("Unfortunately, the username cannot contain consecutive periods (.)")
                    except (IndexError, ValueError):
                        pass
                    finally:
                        if prefix[0] == '\u002E':
                            print("Don't use dot at the start!")
                        else:
                            if prefix[-1] == '\u002E':
                                print("Don't use dot at the end!")
                            else:
                                print('Successful!')

    def __init__(self):
        Link.validate(input('Example of an email address!\nprefix@gmail.com\nEnter your e-mail: '))


y = Link()
