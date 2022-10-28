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

result = int(0)
temp_symbol = ['+','-','*','/']

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