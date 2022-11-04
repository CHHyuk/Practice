def Dataextract(i):
        filepath = 'C:/git/Practice/Python/MyProject/Pokemon_final/Pokemon.txt'
        with open(filepath,'r',encoding='UTF-8') as f: 
            data = f.readlines()
        D = data[i].strip().split() # D = [포켓몬 번호, 이름, 체력, 공격력, 스킬 이름]
        return D