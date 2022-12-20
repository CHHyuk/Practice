def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print('1. 더하기')
print('2. 빼기')
print('3. 곱하기')
print('4. 나누기')

choice = input(' ')

x = int(input('x : '))
y = int(input('y : '))

if choice == '1':
    print(add(x,y))
if choice == '2':
    print(minus(x,y))
if choice == '3':
    print(multiply(x,y))
if choice == '4':
    print(divide(x,y))
    