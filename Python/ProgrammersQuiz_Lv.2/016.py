# 멀리 뛰기 

def solution(n):
    a , b = 0 , 1
    for i in range(n):
        a,b = b, a+b
    return b % 1234567
    







solution(4)