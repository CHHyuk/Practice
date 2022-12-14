# 상속(inheritance) : 물려받다. 물려받은 기능을 유지한 채 다른 기능을 추가하는 기능
# 물려주는 클래스 = 부모클래스
# 물려받는 클래스 = 자식클래스

class person:
    def hi(self):
        print('안녕')

class student(person):
    def study(self):
        print('공부하다.')


jin =  student()
jin.study()
jin.hi()

# 상속 심화 - 호환관계

class person2:
    def hi(self):
        print('안녕')
    

class Add_person:
    def __init__(self):
        self.person_note = [] # 사람 노트는 사람을 갖고있다.
    
    def add_person(self, person):
        self.person_note.append(person)

# Add_person 과 person2 는 동등한 관계가 아니기 때문에(person은 사람, Add_person은 사람을 포함하는 리스트) 상속을 사용할 수 없음

