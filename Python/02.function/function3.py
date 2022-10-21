from tkinter import Y


def print_sqrt(a, b, c): # a, b, c 매개변수
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(x1, x2))

x = 1
y = 2
z = -8

print_sqrt(x, y, z) # x, y, z 실행인자, 매개변수와 같은 갯수의 실행인자를 넣어야 오류없이 실행

x = 1
y = 2
z = -8

print_sqrt(x, y, z)

def print_round(number):
    rounded = round(number)
    print(rounded)

print_round(4.6)
print_round(4.4)
print_round(3.9)