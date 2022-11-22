
"""
list1 = [1,2,3,4]
list1.append(5)
print(list1)

list1.remove(1)
print(list1)

dict1 = {1:'one',2:'two'}
print(dict1)
"""
tuple1 = (1,2,3) # 괄호 해도 되고 안해도 되지만 하는게 더 튜플임을 명확하게 보여줌
print(tuple1)

type(tuple1)

tuple2 = 1,2,3
print(tuple2)

type(tuple2)

list1 = [1,2,3]
tuple3 = tuple(list1)
print(tuple3)

print(tuple3[1])

# tuple3[0] = 5 튜플은 고정값으로 처리하기 때문에 값의 변경과 삭제가 불가능
