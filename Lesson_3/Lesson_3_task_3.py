# Lesson 3 task 3
my_name = "andrei"
while True:                                   # Создаем цикл с истинным условием
    user_name = (input("Enter your name:\n"))
    if my_name == user_name.lower():          # Если имя пользователя совпадает с "моим" именем выводит на экран надпись
        print("Access allowed")
        break                                 # Останаквливает цикл
    else:                                     # Если имя пользователя не совпадает,отказывает в доступе
        print("Access Denied\n")
