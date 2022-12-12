# 비공개 클래스 속성

class Person:
  __weight = 78

  def print_weight(self):
    print(Person.__weight)

jin = Person()
jin.print_weight()

print(jin.__weight)