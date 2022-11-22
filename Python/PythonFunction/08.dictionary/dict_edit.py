
list = [1,2,3,4,5]
print(list)
list[2]=33
print(list)
list.append(6)
print(list)

dict = {'one':1, 'two':2}
print(dict)

dict['one'] = 11
print(dict)

dict['three'] = 3
print(dict)

del(list[0])
del(dict['one'])
print(list)
print(dict)

print(list.pop(0))
print(list)

print(dict['two'])
print(dict.pop('two'))
print(dict)