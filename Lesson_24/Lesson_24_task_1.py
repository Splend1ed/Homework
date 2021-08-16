from typing import Union


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def staked(symbs: Union[str, list, int]):
    stack_obj = Stack()
    if type(symbs) == list:
        conv_to_str = ''
        for i in symbs:
            stack_obj.push(i)
        while not stack_obj.is_empty():
            conv_to_str.join(stack_obj.pop())
        return conv_to_str

    elif type(symbs) == str:
        conv_to_str = ''
        list_of_symbs = symbs.split()
        while not stack_obj.is_empty():
            conv_to_str.join(stack_obj.peek())
        return conv_to_str


staked('123456')
staked([1,2,3,4,5,6])






# def stack_simple_func(start: int, stop: int):
#     list_with_nums = [i for i in range(start, stop + 1)]
#     while list_with_nums != 0:
#         print(list_with_nums.pop())
#
#
# stack_simple_func(1, 20)