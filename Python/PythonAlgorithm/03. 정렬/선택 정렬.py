# 선택 정렬
"""
처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스왑

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 선택 정렬의 시간 복잡도
"""
선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같다
    N + (N - 1) + (N - 2) + ... + 2
이는 (N^2 + N - 2) / 2 로 표현할 수 있으며 빅오 표기법에 따라서 O(N^2)이라고 작성한다.
"""