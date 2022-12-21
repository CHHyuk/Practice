
class User():

    def __init__(self, x, y):
        self.name = ''
        self.monlist_name = []
        self.monlist = []
        self.itemlist = {}
        self.money = 100
        self.x , self.y = x , y
        self.nx, self.ny = x , y
        self.id = 'P'   

    def User_inven(self):
        print(self.name, '님의 인벤토리')
        print('보유 몬스터',self.monlist_name)
        print('보유 아이템',self.itemlist)
        print('보유 돈',self.money)
    
    def move(self, direction):
        if direction == 'w':
            self.nx, self.ny = self.x, self.y - 1
            
        elif direction == 'a':
            self.nx, self.ny = self.x - 1, self.y
            
        elif direction == 's':
            self.nx, self.ny = self.x, self.y + 1
           
        elif direction == 'd':
            self.nx, self.ny = self.x + 1, self.y
        
        a = 0
        b = 0
        for i in gamemap:
            for j in i:
                if a == self.nx and b == self.ny:
                    gamemap[b][a] = self.id
                    
                    print('플레이어 위치 : P \n')
                    print('C : 초원마을 S : 사막마을 M : 물마을 \n')
                    for c in range(len(gamemap)):
                        print(gamemap[c])
                    print('\n')
                    print('\n')
                else:
                    gamemap[b][a] = gamemap_real[b][a]
                a += 1
            b += 1
            a = 0

        if not self.collide():
            self.x, self.y = self.nx, self.ny
            
        
    def collide(self):
        if gamemap[self.ny][self.nx] == 1:
            print('길이 아닙니다.')
            return True
        else:
            print('현재 위치 좌표는','[',self.nx + 1 ,',', self.ny + 1,']','입니다')
            return False






gamemap = [
    ['1','1','1','1','1','1','1'],
    ['1','C','0','0','0','1','1'],
    ['1','0','0','0','0','1','1'],
    ['1','0','0','0','M','1','1'],
    ['1','S','0','0','0','1','1'],
    ['1','0','0','0','0','1','1'],
    ['1','1','1','1','1','1','1']
]

gamemap_real = [
    ['1','1','1','1','1','1','1'],
    ['1','C','0','0','0','1','1'],
    ['1','0','0','0','0','1','1'],
    ['1','0','0','0','M','1','1'],
    ['1','S','0','0','0','1','1'],
    ['1','0','0','0','0','1','1'],
    ['1','1','1','1','1','1','1']
]

