class person:
    def hi(self):
        print('hi')

jin = person()

jin.hi() # 인스턴스를 활용해 메서드 호출

# 정적 메서드
class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def multiple(a,b):
        print(a*b)

Calc.add(10,20) # 클래스에서 바로 메서드 호출
Calc.multiple(10,20)

# 클래스 메서드

class person2:
    count = 0 # 클래스 속성

    def __init__(self):
        person2.count += 1
    
    @classmethod
    def print_count(cls): # 클래스 매서드
        print('사람이 {}명 있습니다.'.format(cls.count)) # cls로 클래스 속성에 접근

paul = person2()
jane = person2()

person2.print_count()