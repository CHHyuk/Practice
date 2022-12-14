# 메서드 오버라이딩 : 부모한테 물려받은 기능을 자식 차원에서 재정의 해서 쓰는 것

class Person:
    def hello(self):
        print('hi 부모')

class Student(Person):
    def hello(self):
        print('hi 자식')

class Worker(Person):
    pass
jin = Student()
jin.hello()
paul = Worker()
paul.hello()
