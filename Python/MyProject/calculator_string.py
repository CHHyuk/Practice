from unittest import result

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

a = input(str)
list = list(a)

for index, x in enumerate(list):
    if index % 2 != 0 and x == '+':
        print(add(list[index-1],list[index+1]))
        break
    elif x == '-':
        print(minus(list[index-1],list[index+1]))
        break
    elif x == '*':
        print(multiply(list[index-1],list[index+1]))
        break
    elif x == '/':
        print(divide(list[index-1],list[index+1]))
        break