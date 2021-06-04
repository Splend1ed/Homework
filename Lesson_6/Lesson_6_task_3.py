# 1 вариант(Также не совсем правельный)

i = tuple(i for i in range(1, 11))
j = tuple(i ** 2 for i in i)
print([i, j])


# 2 вариант(И снова такой же как делали на уроке)
# print([(i, i ** 2) for i in range(1, 11)])
