# 선형 배열(Linear Array)
"""
배열 : 같은 자료형을 가진 데이터가 연속적으로 저장된 자료구조
"""

# 리스트 관련 메서드
"""
리스트 길이와 실행 시간이 상관 없는 메서드
"""
list = []
iterable = 0 # 예시
list.append(iterable) # 맨 뒤의 원소로 그대로 덧붙이기
list.extend(iterable) # 맨 뒤에 원소로 추가하기
list.pop() # 맨 뒤의 원소 하나를 꺼내기

# append와 extend의 차이
list1 = ['A', 'B', 'C']
list2 = ['D', 'E']
# append
list1.append(list2)
print(list1) # ['A', 'B', 'C', ['D', 'E']]
# extend
list1.extend(list2)
print(list1) # ['A', 'B', 'C', 'D', 'E']

"""
리스트 길이와 실행 시간에 비례하는 메서드 (O(n))
"""
index = 0 # 예시
list.insert(index,iterable) # 특정 index에 원소 추가
del(index)
del list[index] # 특정 위치 원소 삭제
list.index(data) # 특정 값(data)이 존재하는 위치를 돌려줌

