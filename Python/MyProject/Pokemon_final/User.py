
class User():

    def __init__(self, x, y):
        self.name = ''
        self.monlist_name = []
        self.monlist = []
        self.itemlist = {}
        self.money = 0
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
            for i in gamemap:
                print(i)
        elif direction == 'a':
            self.nx, self.ny = self.x - 1, self.y
            for i in gamemap:
                print(i)
        elif direction == 's':
            self.nx, self.ny = self.x, self.y + 1
            for i in gamemap:
                print(i)
        elif direction == 'd':
            self.nx, self.ny = self.x + 1, self.y
            for i in gamemap:
                print(i)

        if not self.collide():
            self.x, self.y = self.nx, self.ny
            
        
    def collide(self):
        if gamemap[self.ny][self.nx] == '1':
            print('길이 아닙니다.')
            return True
        else:
            print('현재 위치 좌표는','[',self.nx + 1 ,',', self.ny + 1,']','입니다')
            return False





































gamemap = [
        ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
        ['1','1','1','1','0','0','0','0','0','0','0','1','1'],
        ['1','C','0','0','0','0','0','0','0','0','0','1','1'],
        ['1','0','0','0','0','M','0','0','0','0','0','1','1'],
        ['1','0','0','0','0','0','0','0','0','0','0','1','1'],
        ['1','0','0','0','0','0','0','0','0','0','0','1','1'],
        ['1','0','0','0','0','0','0','0','0','0','0','1','1'],
        ['0','0','0','0','0','0','0','0','0','0','0','1','1'],
        ['0','S','0','1','1','1','1','0','0','0','0','1','1'],
        ['0','0','0','1','1','1','1','0','0','0','0','1','1'],
        ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ]
