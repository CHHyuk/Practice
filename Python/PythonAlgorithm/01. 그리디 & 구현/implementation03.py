# 왕실의 나이트
"""
행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면이다.
왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 말을 타고 있어 이동을 할 때는 L자 형태로만 이동할 수 있으며
정원 밖으로는 나갈 수 없다
나이트의 이동 방법
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
나이트의 위치가 주어질 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성
"""

# 현재 나이트의 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동 할 수 있는 8가지 방향 정의
steps = [(-2, -1),(-1 , -2),(1, -2),(2, -1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result +=1

print(result)