# 상속 속성

class Person:
    def __init__(self):
        print('Person __init__ 호출됨')
        self.hello = '안녕'

class Student(Person):
    def __init__(self):
        print('Student __init__ 호출됨')
        super().__init__()
        self.school = 'Korea IT'

jin = Student()
print(jin.school)
print(jin.hello)