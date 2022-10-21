for a in [0, 1, 2, 3, 4]:
    print(a)

for b in range(10):
    print(b)

names = ['A', 'B', 'C', 'D']

for c in range(4):
    name = names[c]
    print('{}번: {}'.format(c + 1, name))

for c, name in enumerate(names):
    print('{}번: {}'.format(c + 1, name))

#for c in range(11172):
#    print(chr(44032 + c), end=' ')