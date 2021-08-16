class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return 'woof woof'


class Cat(Animal):
    def talk(self):
        return 'meow'


def talking(animals):
    print(animals.talk())


cat = Cat()
dog = Dog()
talking(cat)
talking(dog)
