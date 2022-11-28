"""
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
"""

n, m = map(int,input().split())

sum = []
temp = []
answer = []
for i in range(2):
    for j in range(m):
        sum.append(list(map(int, input().split())))

for x in range(n):
    for y in range(n):
        temp.append(sum[x][y] + sum[x+n][y])
    print(*temp)
    temp = []