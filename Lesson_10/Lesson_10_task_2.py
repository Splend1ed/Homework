class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age_factor * self.age


question = int(input('How old is your dog?\n'))
dog_age = Dog(question)
print(dog_age.human_age())
