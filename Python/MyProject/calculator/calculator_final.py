import re

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

result = int(0)
temp_symbol = ['+','-','*','/']

exp = input('식을 입력하세요> ')
list = re.split('([-|+|*|/])',exp)

for index, x in enumerate(list):
    if index == 0:
        result = int(x)          
    elif x in temp_symbol:
        if x == '+':
            result = add(result,int(list[index+1]))
        elif x == '-':
            result = minus(result,int(list[index+1]))
        elif x == '*':
            result = multiply(result,int(list[index+1]))
        elif x == '/':
            result = divide(result,int(list[index+1]))

print(result)