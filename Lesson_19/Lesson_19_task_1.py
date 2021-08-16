from time import gmtime, strftime


class ConManager:
    counter = 0

    def __init__(self, file_name: str, mode='r'):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        ConManager.counter += 1
        with open('LogMyConManager.txt', 'w+') as log:
            log.write(f'-File with name {self.file_name} was opened {ConManager.counter} '
                      f'number of times at such a time {strftime("%Y-%m-%d %H:%M:%S", gmtime())}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.file.close()
        except exc_type:
            with open('LogMyConManager.txt', 'w') as log:
                if exc_val:
                    log.write(f'File crashed in {strftime("%Y-%m-%d %H:%M:%S", gmtime())}'
                              f' with this exceptions: {exc_type}: {exc_tb}')
                else:
                    log.write(f'File was closed in {strftime("%Y-%m-%d %H:%M:%S", gmtime())}.All good!')



mycon = ConManager('test.txt', 'w')

with mycon as file:
    file.write('123')



