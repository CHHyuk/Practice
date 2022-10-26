list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = list(range(10))

print(list2)

del list2[0]

print(list2)

print(list2[:5])

del list2[:5]
print(list2)

print(list2[1:3])

list2[1:3] = [77,88,99,1010]
print(list2)

list2[1:4] = [18]
print(list2)