class WithIndex:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.with_index_list = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iterable) > self.start:
            self.with_index_list.append((self.start, self.iterable[self.start]))
            self.start += 1
            return self.with_index_list
        else:
            raise StopIteration


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = WithIndex(list1)
for i in list2:
    print(i)