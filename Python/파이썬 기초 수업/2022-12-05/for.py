# 문제 : for문으로 1부터 100까지 출력

for i in range(1,101):
    print(i)

# 문제 : for문으로 100부터 1까지 출력
for i in range(100,0,-1):
    print(i)

# 문제 : for문으로 1부터 100 사이의 짝수만 출력
for i in range(2,101,2):
    print(i)

# 문제 : for문으로 100부터 1 사이의 짝수만 출력
for i in range(100,0,-2):
    print(i)

# 문제 : for문으로 구구단 8단 출력
for i in range(1,10):
    print('{} * {} = {}'.format(8,i,8*i))

# 문제 : for문으로 구구단 1단 ~ 9단 출력
for i in range(2,10):
    print ('==={}단==='.format(i))
    for j in range(1,10):
        print ('{} * {} = {}'.format(i,j,i*j))

# 문제 : for문으로 1부터 n사이에 존재하는 소수의 합을 반환하는 함수 구현
def prime_number(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
n = 10
result = 0
for i in range(1,n+1):
    if prime_number(i):
        result += i
print(result)