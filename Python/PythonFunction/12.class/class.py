# class는 자기소개서다.

class student:
    def __init__(self): # initiate, 클래스를 선언하는 순간 실행되는 함수
                        # self : 본인, 클래스를 저장할 변수
        self.name = input("이름 : ")
        self.age = input('나이 : ')
        self.major = input('전공 : ')
    def show(self):
        print('나의 이름은 {}, 나이는 {}세 이고, 전공은 {}입니다.'.format(self.name,self.age,self.major))


CHH = student() # CHH = 클래스 안의 self에 해당
CHH.name # init 함수의 self.name에 해당, 초기에 설정된 name 부분
CHH.age # init 함수의 self.age에 해당
CHH.major # init 함수의 self.major에 해당
CHH.show() # CHH에 해당하는 show 함수 실행, 

class student2(student):
    def __init__(self):
        super().__init__() # 기존 student 클래스의 init 함수 내의 내용 가져옴
        self.gender = input('성별 : ')
    def show(self):
        print('나의 이름은 {}, 나이는 {}세, 성별은 {}, 전공은 {}입니다.'.format(self.name,self.age,self.gender,self.major))

CHH = student2()
CHH.show()