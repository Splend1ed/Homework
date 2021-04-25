import random


list1 = []
list2 = []
while len(list1) < 10 and len(list2) < 10:
    randomizer = random.randint(1, 10)
    list1.append(randomizer)
    list2.append(randomizer)
print("First list: " + str(list1) + "\n" + "Second list: " + str(list2))
conversion1 = set(list1)
conversion2 = set(list2)
list3 = conversion1.intersection(conversion2)
print("Third list: " + str(list(list3)))
