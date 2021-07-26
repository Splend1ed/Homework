


def count_lines(file_name: str):
    try:
        with open(file_name, 'r') as file:
            line_count = file.readlines()
        return len(line_count)
    except (FileNotFoundError, FileExistsError):
        print('File not found, or file hard-coded')


def count_chars(file_name):
    try:
        with open(file_name, 'r') as file:
            chars_amount = file.read()
            chars_amount.strip(' ')
        return len(chars_amount)
    except (FileNotFoundError, FileExistsError):
        print('File not found, or file hard-coded')


def test(file_name):
    return f'Line amount: {count_lines(file_name)}\nChars amount: {count_chars(file_name)}'

print(test('asd.py'))
