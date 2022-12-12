class person():
    def __init__(self, name, age, hobby):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.hobby = hobby
        
    def introduce(self):
        print('{}, 저는 {}입니다'.format(self.hello,self.name))


jin = person('진',23,'농구')
jin.introduce()

print('이름 : {}'.format(jin.name))
print('나이 : {}'.format(jin.age))
print('취미 : {}'.format(jin.hobby))

paul = person('폴',25,'축구')
paul.introduce()

print('이름 : {}'.format(paul.name))
print('나이 : {}'.format(paul.age))
print('취미 : {}'.format(paul.hobby))