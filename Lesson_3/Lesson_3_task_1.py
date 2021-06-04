# Lesson 3 task 1
string = (input("Write your message\n"))    # Ввод сообщения пользователя
print("Line length:", len(string))          # Измерение и вывод на экран пользователя длины строки
if len(string) > 2:                         # Если длина строки больше 2 символов получаем строку из первых двух
    print(string[:2] + (string[-2:]))       # символов и последних двух
elif len(string) == 2:                      # Если длина строки 2 символа умножаем строку на 2
    print(string * 2)
else:                                       # Если длина строки меньше 2 символов получаем пустую строку
    print("Empty string")
