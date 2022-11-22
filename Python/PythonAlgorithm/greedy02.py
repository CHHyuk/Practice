# 1이 될 때까지
"""
어떠한 수 N이 1이 될 때 까지 두 과정 중 하나를 반복적으로 선택하여 수행
단 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택 가능
    1. N에서 1을 뺍니다
    2. N을 K로 나눕니다
N과 K가 주어질 때 N이 1이 될 때 까지 1번 혹은 2번 과정을 수행해야 하는 최소 횟수를 구하시오
"""
n, k = map(int,input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k # 나누어 떨어지는 수 target
    result += (n - target) # 1을 빼는 연산 횟수 result
    n = target
    # N이 K보다 작을때(더 이상 나눌 수 없을때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)