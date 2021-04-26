list1 = []
list2 = []
i = 0
n = 0
while i < 100:
    i += 1
    if i % 7 == 0 and i % 5 != 0:
        list2.append(i)
    list1.append(i)
print(list1)
print(list2)
