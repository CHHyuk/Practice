# 정렬된 배열에서 특정 수의 개수 구하기
"""
N개의 원소를 포함하는 수열이 오름차순으로 정렬되어 있을때 수열에서 x가 등장하는 횟수를 계산하라
예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2 이면 4를 출력한다
단 이 문제는 시간 복잡도 O(logN)로 알고리즘 설계하지 않으면 시간 초과 판정을 받는다
"""

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array,right_value)
    left_index =  bisect_left(array,left_value)
    return right_index - left_index

n, x = map(int,input().split()) # 데이터의 개수 N, 찾고자 하는 값  x 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)