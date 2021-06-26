class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.first_name.title()} {self.last_name.title()} and i`m {self.age} years old')


person_objects = Person(input('Enter your first name: '), input('Enter your last name: '), input('Enter your age: '))

print(person_objects.talk())
