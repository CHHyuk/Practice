# 클래스 : 객체를 사용하기 위한 문법의 일종, 프로그래밍으로 객체를 만들 때 사용함
"""
ex) 전사, 마법사, 궁수, 자동차, 비행기, 사람, 강아지, 고양이, 버튼 등 > Object(객체)
위의 객체들을 표현하는 도구 > 클래스
현실, 가상, 개념 등
"""

class character:
    def __init__(self):
        self.name = '피카츄'
        self.exp = 0
        self.level = 1

    def training(self):
        self.exp += 1
        print('{}이(가) 훈련을 했다, {}의 경험치 +1, 현재 경험치 {} / 100'.format(self.name,self.name,self.exp))
        if self.exp >= 100:
            print('{} 레벨업!'.format(self.name))
            self.level += 1
            self.exp = 0
        
    def status(self):
        print('===={} 상태창===='.format(self.name))
        print('레벨 : {}'.format(self.level))
        print('경험치 : {}'.format(self.exp))

x = character()

flag = True
while flag:
    print('=== UI ===')
    choice = input('1.상태창 2.훈련 > ')
    if choice == '1':
        x.status()
    elif choice == '2':
        x.training()
