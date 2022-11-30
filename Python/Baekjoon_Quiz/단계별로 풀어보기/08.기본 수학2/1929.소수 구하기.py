"""xxxxxxxx
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
에라스토테네스의 체
"""

def prime_number(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

m,n = map(int,input().split())

check = [True] * n

