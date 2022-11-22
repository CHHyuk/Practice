# 구현 알고리즘
# 상하좌우
"""
여행가 A 는 N x N 크기의 정사각형 공간에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다
여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며 시작 좌표는 항상 (1,1)이다.
여행가가 계획표 (U,R,L,D) 대로 움직인다고 할때
N과 계획표가 주어질 때 여행가 A의 도착지점의 좌표 입력
"""

n = int(input())
x, y = 1, 1
plans = input().split()

# U, D, L, R에 따른 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U','D','L','R']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x,y)
