filepath = 'C:/git/Practice/Python/00.vscode/Pokemon.txt'
with open(filepath,'r',encoding='UTF-8') as f: 
    data = f.readlines()

P = data[0].strip().split()

print(P)