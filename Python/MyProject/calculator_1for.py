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
temp_symbol = ['+','-','*','/']

for index, x in enumerate(list):
    if 