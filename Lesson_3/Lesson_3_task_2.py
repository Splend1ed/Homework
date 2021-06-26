# Lesson 3 task 2
while True:                                                     # Создаем цикл с истинным условием
    phone_number = (input("Enter the phone number:"))           # Ввод номера телефона пользователя
    if len(phone_number) == 10:                                 # Проверка на количество символов в номере
        print("All good!")
        break                                                   # Остановка цикла
    else:                                                       # Если в номере меньше или больше цифр,выдает ошибку
        print(input("Something went wrong.\n"))
