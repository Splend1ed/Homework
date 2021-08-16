from fractions import Fraction


class MyFraction:
    def __init__(self, num):
        num = num.split("/")
        self.num = Fraction(int(num[0])) / Fraction(int(num[1]))

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __truediv__(self, other):
        return other.num / self.num

    def __mul__(self, other):
        return self.num * other.num


x = MyFraction("3/2")
y = MyFraction("1/3")
print(x + y)
print(x - y)
print(x / y)
print(x * y)

