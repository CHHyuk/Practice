list2 = [37, 23, 10, 33, 28, 124]
print(list2)

list2.append(16)
print(list2)

list3 = list2 + [16]
print(list3)

list4 = list2 + list3
print(list4)

n = 12
ownership = n in list3
print(ownership)

n = 10
ownership = n in list3
print(ownership)


if n in list3:
    print('{}은 있어!'.format(n))

print(list4)
del(list4[12])
print(list4)
list4.remove(33)
print(list4)