import random


# Создание пустого листа и цикла который проверяет длину списка и добавляет в него 1 рандомное число от 1 до 10
list2 = []
while len(list2) < 10:
    randomizer = random.randint(1, 10)
    list2.append(randomizer)
print("This is your largest number from a randomly generated list: " + str(max(list2)))
print("This is a randomly generated list: " + str(list2))
