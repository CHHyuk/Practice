
def root(a, b, c):
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return x1, x2

x = 1
y = 2
z = -8

x1, x2 = root(x, y, z)
print('근은 {} {}'.format(x1, x2))

# 함수의 return
# 함수는 return을 이용해 값을 돌려줄 수 있다