def print_sqrt():
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(x1, x2))

a = 1
b = 2
c = -8

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('해는 {} 또는 {}'.format(x1, x2))

a = 1
b = 2
c = -8

print_sqrt()