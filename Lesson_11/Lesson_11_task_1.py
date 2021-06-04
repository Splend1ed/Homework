class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def person_have(self):                                              # Общий метод
        print(f'''
Person have a first name: {self.first_name} 
Person have a last name: {self.last_name}
Person have gender: {self.gender}
Person have age: {self.age}
''')


class Student(Person):
    def __init__(self, first_name, last_name, gender, age, partying, study):
        self.partying = partying
        self.study = study
        super().__init__(first_name, last_name, gender, age)

    def student_can(self):
        print(f'Student can {self.partying} and {self.study}')


class Teacher(Person):
    def __init__(self, first_name, last_name, gender, age, payday, experience, teach):
        self.payday = payday
        self.experience = experience
        self.teach = teach
        super().__init__(first_name, last_name, gender, age)

    def teacher_have_and_can(self):
        print(f'Teacher have {self.payday}, {self.experience} and they can {self.teach} Student')


s = Student("Grisha", 'Kovalenko', 'male', 22, "tysit", 'zybrit')
t = Teacher('Tatiana', 'Jyrova', 'female', 53, '250$', '30 years exp', 'teach')
s.person_have()
s.student_can()
t.person_have()
t.teacher_have_and_can()
