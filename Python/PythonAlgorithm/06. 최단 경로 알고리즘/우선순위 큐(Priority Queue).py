# 특징
"""
    우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료 구조
    예) 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터
    꺼내서 확인해야 하는 경우 이용 가능
    대부분 프로그래밍 언어에서 표준 라이브러리 형태로 지원
    
    스택 : 가장 나중에 삽입된 데이터가 추출
    큐 : 가장 먼저 삽입된 데이터가 추출
    우선순위 큐 : 가장 우선순위가 높은 데이터가 추출
"""

# 힙(Heap)
"""
    우선순위 큐를 구현하기 위해 사용하는 자료 구조 중 하나
    최소 힙(Min Heap)과 최대 힙(Max Heap)이 있다
    다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용

    우선순위 큐를 리스트로 구현하면
    삽입 시간 : O(1)    삭제 시간 : O(N)
    우선순위 큐를 힙으로 구현하면
    삽입 시간 : O(logN) 삭제 시간 : O(logN)
"""

# 힙 라이브러리 사용 예제: 최소 힙

import heapq

# 오름차순 힙 정렬(heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result) # [0,1,2,3,4,5,6,7,8,9]