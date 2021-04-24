import random                                                         # Импорт модуля


check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                          # Создаем список с 10-ю объектами внутри
list1 = []                                                            # Создаем 1 пустой список
list2 = []                                                            # Создаем 2 пустой список
while True:                                                           # Создаем цикл
    while len(list1) <= len(check_list):                              # Создаем проверочный цикл для 1 списка
        randomizer = random.randint(1, 10)                            # Генерация рандомного числа с 1 до 10
        list1.append(randomizer)                                      # Добавление объекта в конец списка 1
    while len(list2) <= len(check_list):                              # Создаем проверочный цикл для 2 списка
        randomizer = random.randint(1, 10)                            # Генерация рандомного числа с 1 до 10
        list2.append(randomizer)                                      # Добавление объекта в конец списка 2
    print("First list: " + str(list1) + "\n" + "Second list: " + str(list2))    # Вывод 1 и 2 списка
    break                                                                       # Остановка цикла
conversion1 = set(list1)                                              # Конвертация списка1 в tuple
conversion2 = set(list2)                                              # Конвертация списка2 в tuple
list3 = conversion1.intersection(conversion2)                         # Пересичение объектов
print("Third list: " + str(list(list3)))                              # Вывод 3 строки
