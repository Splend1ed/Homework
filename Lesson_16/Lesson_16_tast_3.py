class MyIteration:
    def __init__(self, entry_list):
        self.entry_list = entry_list

    def __getitem__(self, index):
        return self.entry_list[index]


my_list = MyIteration([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in my_list:
    print(i)

print(my_list[2])
