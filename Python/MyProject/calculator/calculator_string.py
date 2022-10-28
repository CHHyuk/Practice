from unittest import result

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

my_list = input(str)
list = list(my_list)

for index, x in enumerate(my_list):
    if index % 2 != 0 and x == '+':
        print(add(int(list[index-1]),int(list[index+1])))
    elif x == '-':
        print(minus(int(list[index-1]),int(list[index+1])))
    elif x == '*':
        print(multiply(int(list[index-1]),int(list[index+1])))
    elif x == '/':
        print(divide(int(list[index-1]),int(list[index+1])))