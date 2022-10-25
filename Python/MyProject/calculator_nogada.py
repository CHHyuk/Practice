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

result = 0

for index, x in enumerate(my_list):
    if index == 1 and x == '+':
        result1 = add(int(list[0]),int(list[2]))
    elif x == '-':
        result1 = minus(int(list[0]),int(list[2]))
    elif x == '*':
        result1 = multiply(int(list[0]),int(list[2]))
    elif x == '/':
        result1 = divide(int(list[0]),int(list[2]))
    elif index == 2:
        break

for index, x in enumerate(my_list):
    if index == 3 and x == '+':
         result2 = add(result1,int(list[index+1]))
    elif x == '-':
        result2 = minus(result1,int(list[4]))
    elif x == '*':
        result2 = multiply(result1,int(list[index+1]))
    elif x == '/':
        result2 = divide(result1,int(list[index+1]))
        
print(result2)
