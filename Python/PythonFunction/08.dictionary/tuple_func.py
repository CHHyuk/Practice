
list = [1,2,3,4,5]
for i, v in enumerate(list):
    print('{}번째 값: {}'.format(i,v))


list = [1,2,3,4,5]
for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))

ages = {'Tod':35, 'Jane':23, 'Paul':62}
for key,val in ages.items():
    print('{}의 나이는 : {}'.format(key,val))

ages = {'Tod':35, 'Jane':23, 'Paul':62}
for a in ages.items():
    print('{}의 나이는 : {}'.format(*a))