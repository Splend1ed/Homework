import random


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                                    # Создаем 1 список с 10-ю объектами внутри
list2 = []                                                                                  # Создаем 2 список пустой
while True:                                                                                            # Создаем цикл
    while len(list2) <= len(list1):                                                      # Сохдаем 2 проверочный цикл
        randomizer = random.randint(1, 10)                                     # Генерация рандомного числа с 1 до 10
        list2.append(randomizer)                                        # Добавление рандомного числа в список "list2"
    print("This is your largest number from a randomly generated list: " + str(max(list2)))  # Вывод на экран самого
    break                                                                                    # большого числа с списка