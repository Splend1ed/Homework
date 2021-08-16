class InRange:
    def __init__(self, start=0, end=None, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.zero = 0

    def __iter__(self):
        return self

    def __next__(self):
        values1 = self.zero
        values2 = self.start
        if self.end is None:
            if self.zero < self.start:
                self.zero += self.step
                return values1
            else:
                raise StopIteration
        else:
            if self.start < self.end:
                self.start += self.step
                return values2
            else:
                raise StopIteration


range_ = InRange(1, 20, 2)
for i in range_:
    print(i)
