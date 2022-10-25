#packing : 하나의 변수에 여러 개의 값을 넣는 것
#unpacking : 패킹된 변수에서 여러 개의 값을 꺼내오는 것

from re import X


a, b = 1, 2
print(a) # 1
print(b) # 2

c = (3,4)
print(c)

d, e = c

print(d) # 3
print(e) # 4

f = d,e
print(f) # f = (3,4) 변수 d,e 를 f에 패킹한 것

x = 5
y = 10
temp = x
x = y
y = temp

print(x) # 10
print(y) # 5

x,y = y,x # x와 y를 다시 바꿨음, temp라는 변수 사용하지 않아도 편리하게 바꿀 수 있음
print(x) # 5
print(y) # 10

def tuple_func():
    return 1,2

q,w = tuple_func()
print(q) # tuple_func 에서 리턴된 값 1
print(w) # tuple_func 에서 리턴된 값 2