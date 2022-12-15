# 정렬과 탐색 (Sorting & Searching)

# 선택 정렬 ===========================
"""
동작 순서
1. 현재 리스트에서 최소값을 찾는다.
2. 그 값을 첫번째 인덱스 값과 교환한다.
3. 첫 원소를 제외한 나머지 리스트를 기준으로 다시 1번으로 돌아가 정렬한다.
"""

# 예시 코드
TEST = [9, 4, 3, 7, 10, 22, 1,  6]

# 첫 원소 ~ 가장 마지막 원소를 제외한 원소까지
for i in range(len(TEST)-1):
    
    # 가장 작은 원소의 인덱스를 시작 지점으로 설정
    min_idx = i

    # 시작 원소의 다음 원소 부터 배열 끝까지 값 탐색
    # 가장 작은 인덱스를 찾는다.
    for j in range(i+1, len(TEST)):
        if TEST[min_idx] > TEST[j]:
            min_idx = j

    # 1번 탐색마다 각 배열의 범위에서 가장 작은 인덱스와 시작 인덱스를 변경한다.
    TEST[i], TEST[min_idx] = TEST[min_idx], TEST[i]

print(TEST)

"""
1. 최악 시간복잡도 (O(N^2))
배열이 역 정렬 상태일 경우

2. 최선 시간복잡도 (O(N^2))
배열이 이미 정렬되어 있을 때도, 최소값을 찾기 위해 동일하게 탐색을 해야한다.
"""

# 버블 정렬 ===========================
"""
동작 순서
1. 현재 인덱스와 다음 인덱스를 비교하여, 현재 인덱스가 더 큰 경우 스왑한다.
2. 현재 인덱스의 값이 len(iterator) - 1 일 때까지 반복한다. 마지막 인덱스일 경우 다음 인덱스와 비교가 불가능하기 때문이다.
3. 매 정렬마다 비교한 iterator의 마지막 부분이 정렬 범위 중 가장 큰 값이기 때문에, 다음 정렬은 첫 인덱스 ~ 이전 정렬의 마지막 부분을 제외한 부분 까지로 지정한다.
    a. 즉, 이전의 정렬 범위가 i 인덱스였다면 다음 정렬 탐색 범위는 iterator[:i] 가 된다.
"""

# 예시 코드

TEST = [9, 4, 3, 7, 10, 22, 1,  6]

for i in range(len(TEST)-1):
    
    # 한번 끝까지 정렬을 완료하면, 가장 큰 수는 무조건 맨 뒤에 위치하기 한다.
    # 따라서 다음 정렬에서는 배열의 범위를 하나씩 줄여준다.
    # 이를 1부터 (배열 전체 길이-1)까지 증가하는 i 값으로 만들어준다.
    for i in range(len(TEST)):

        # 이전 값을 비교하기 위해 1번 인덱스부터 시작
        for j in range(1, len(TEST) - i):

            # 이전 값이 더 클경우 swap
            if TEST[j - 1] > TEST[j]:
                TEST[j - 1], TEST[j] = TEST[j], TEST[j - 1]

print(TEST)

"""
1. 최악 시간복잡도 (O(N^2))
배열이 역 정렬 상태일 경우

2. 최선 시간복잡도 (O(N^2))
배열이 정렬 상태일 경우에도 동일하게 비교를 진행해줘야 한다
"""

# 버블 정렬 ===========================
"""
동작 순서
1. 현재 인덱스(i)가 처음인덱스(0) ~ 자신의 바로 앞 인덱스(i-1)중 어디에 삽입되야되는지 확인한다.
삽입 위치를 확인하기 위해, (i-1) 인덱스 → 0 인덱스 순으로 비교하며, 현재 인덱스(i) 값이 더 작을 경우 스왑한다.
만약 스왑을 하지 않게 된다면, 이후 탐색을 하지 않고, 바로 i → i+1 로 변경해준다. (다음 탐색 진행)
EX) 현재 인덱스가 3일때 아래와 같이 진행된다.
    a. 2번 인덱스와 비교하여, 현재(3)인덱스가 더 작을 경우 스왑
        i.만약 현재(3)인덱스가 더 클 경우(스왑할 필요가 없을 경우), 이후 나머지 인덱스는 탐색하지 않는다.
        ii.스왑을 하게되면 다음 비교 인덱스를 탐색한다. (1, 0 ... )
2. 위 과정을 두 번째 인덱스(1)부터 마지막 인덱스(n)까지 반복한다.
"""

# 예시 코드
def insert(array):

    # 앞 인덱스를 비교해야하기 때문에 1번 인덱스 부터 진행
    for i in range(1, len(array)):

        # 현재 인덱스
        idx = i

        # 이전 인덱스보다 작으며, idx가 0보다 클 경우 계속 스왑하며 비교 인덱스를 줄여나간다.
        while array[idx - 1] > array[idx] and idx > 0:
            array[idx - 1], array[idx] = array[idx], array[idx - 1]
            idx -= 1

"""
1. 최악 시간복잡도 (O(N^2))
배열이 역 정렬 상태일 경우

2. 최선 시간복잡도 (O(N))
배열이 정렬되어 있을 경우, 각 인덱스마다 1번씩만 비교를 한다.
"""

# 퀵 정렬 ===========================
"""
동작 순서
1. 첫 번째 원소를 피벗으로 설정한다.
2. 두 번째 원소 위치를 left, 마지막 원소 위치를 right로 설정한다.
    left는 배열의 뒤쪽으로, right는 배열의 앞쪽으로 이동하며 값을 탐색한다.
3. left 위치의 값이 피벗보다 클 때 & right 위치의 값이 피벗보다 작을 때 left와 right 위치의 값을 바꿔준다.
    이 과정을 거쳐 피벗보다 작은 값은 배열 앞쪽에, 피벗보다 큰 값은 배열 뒤쪽에 위치한다.
4. 모든 구분이 끝나면 피벗보다 작은 값들중 가장 큰 값의 위치와 피벗과 바꿔준다.
5. 피벗을 기준으로 왼쪽과 오른쪽 배열로 나눠, start와 end를 설정한 두 재귀함수를 동작시킨다.
"""

# 예시코드 1 = 첫 원소를 피벗으로 사용하는 경우 → 정렬 / 역정렬된 배열일 경우 최악의 경우가 되며 오랜 시간이 소요
def quick_sort(array, start, end):

    # 탐색 원소 범위가 1개일경우
    if end - start < 1:
        return

    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1  # 2번째 원소
    right = end  # 마지막 원소까지

    while left <= right:

        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        if left <= right:
            array[left], array[right] = array[right], array[left]

    # 구분이 끝난 후, 피벗과 변경해준다.
    array[right], array[pivot] = array[pivot], array[right]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


TEST = [4, 2, 3, 5, 6, 7]
quick_sort(TEST, 0, len(TEST) - 1)
print(TEST)

# 예시코드 2 = 매번 피벗을 랜덤으로 지정하는 경우 → 최악의 경우가 거의 발생하지 않음 (거의 불가능)

import random

def quick_sort(array, start, end):

    # 탐색 원소 범위가 1개일경우
    if end - start < 1:
        return

    pivot = random.randint(start, end)  # 피벗은 랜덤한 인덱스로 선택한다.
    left = start  # 2번째 원소
    right = end  # 마지막 원소까지

    # 랜덤하게 선택된 피벗을 가장 첫 인덱스와 자리를 바꾼다.
    array[left], array[pivot] = array[pivot], array[left]

    while left <= right:

        # 가장 첫 인덱스에 존재하는 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[start]:
            left += 1

        # 가장 첫 인덱스에 존재하는 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[start]:
            right -= 1

        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        if left <= right:
            array[left], array[right] = array[right], array[left]

    # 구분이 끝난 후, 피벗과 변경해준다.
    array[start], array[right] = array[right], array[start]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

TEST = [4, 2, 3, 5, 6, 7]
quick_sort(TEST, 0, len(TEST) - 1)
print(TEST)

"""
1. 최악 시간복잡도 (O(N^2))
피벗을 첫번째 원소로 사용하기 때문에, 정렬 / 역정렬 상태일경우 구분의 의미가 없어진다.

2. 최선 시간복잡도 (O(NlogN))
피벗을 잘만 고른다면 정렬 / 역정렬 상태일 경우에도 시간 복잡도를 줄일 수 있다.
최선의 경우는 모든 피벗이 정확히 중간 값으로 설정되어, 모두 절반씩 분할되는 경우이다.
"""
# 퀵 정렬을 효과적으로 사용하기 위한 피벗 설정
"""
피벗을 어떻게 고르냐에 따라 이후 작업의 시간이 결정되며, 상황에 맞게 피벗을 고르는게 매우 중요하다. 
아래 블로그에서는 퀵 정렬의 시간 복잡도를 줄이기 위한 피벗 설정에 대한 좋은 의견을 작성해주셨다.
정리하자면 아래와 같다.

개인적으로 배열이 그렇게 길지 않다면 1번, 배열이 좀 긴편이라면 2번이 좋은 방법 같다.
1번은 초기에 한번만 하면 되고, 2번은 매 피벗 지정마다 해야한다.
1. 정렬하고자 하는 배열을 랜덤화 시켜준다. 즉 한번 뒤섞고 정렬을 해주는 것인데, 이러면 어떤 원소를 피벗으로 사용해도 최악의 시간 복잡도는 막을 수 있다.
    처음 랜덤화를 위해 최소 O(N)O(N) 만큼의 시간을 더 사용하기 때문이다.
    또한 파이썬은 random.shuffle(array) 로 배열을 섞을 수 있다.
예시
"""
def quick_sort(array, start, end):

    ...


TEST = list(range(10000)) # WORST
TEST2 = [random.randint(0, 10000) for _ in range(10000)] # NOT WORST

start_time = time.time()
quick_sort(TEST, 0, len(TEST) - 1)
end_time = time.time()
print("{} sec".format(end_time - start_time))

start_time = time.time()
quick_sort(TEST2, 0, len(TEST2) - 1)
end_time = time.time()
print("{} sec".format(end_time - start_time))
"""
결과는 놀랍다. 최악의 경우는 2.9초가 걸렸지만, 랜덤으로 정렬된 배열은 0.01초가 걸렸다.
10000개의 숫자로 이루어진 배열에서도 이렇게 차이가 나는데, 더 많은 데이터라면 아찔하다.
"""
"""
2. 고정된 위치에서 피벗을 선택하지 않고, 매 정렬 시 피벗 위치를 랜덤으로 선택하는 것이다.
예시
"""
def quick_sort(array, start, end):

    # 탐색 원소 범위가 1개일경우
    if end - start < 1:
        return

    pivot = random.randint(start, end)  # 피벗은 랜덤한 인덱스로 선택한다.
    left = start  # 2번째 원소
    right = end  # 마지막 원소까지

    # 랜덤하게 선택된 피벗을 가장 첫 인덱스와 자리를 바꾼다.
    array[left], array[pivot] = array[pivot], array[left]

    while left <= right:

        # 가장 첫 인덱스에 존재하는 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[start]:
            left += 1

        # 가장 첫 인덱스에 존재하는 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[start]:
            right -= 1

        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        if left <= right:
            array[left], array[right] = array[right], array[left]

    # 구분이 끝난 후, 피벗과 변경해준다.
    array[start], array[right] = array[right], array[start]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


TEST = list(range(10000))

start_time = time.time()
quick_sort(TEST, 0, len(TEST) - 1)
end_time = time.time()
print("{} sec".format(end_time - start_time))
"""
이전에 첫 번째 위치의 인덱스를 피벗으로 사용하는 방식에서는 정렬 / 역정렬된 배열에서 최악의 경우 정렬에 2.9초가 걸렸다.
하지만 피벗을 매번 랜덤으로 설정하게 되면서, 매우 정렬이 빨라진것을 확인할 수 있다.
(2.9초 → 0.015초)
"""
"""
3. 마지막은 피벗의 후보를 3개를 뽑아서 그 중 중간값을 선택하는 방법이다.
"""

# 병합(합병) 정렬 ===========================
"""
동작 순서
1. 배열을 반으로 계속 나누며, 각 배열이 1개의 원소를 가질때까지 반복한다.
2. 이제 나눠진 배열을 하나로 합치며, 작은 원소값이 앞에 오도록 합쳐준다.
3. 2번 과정에서 합쳐진 다른 배열들끼리 다시 비교하여 작은 원소값이 앞에 오도록 합쳐진 배열을 만들어준다.
4. 3번 과정을 반복한다. → 3번 과정으로 배열이 합쳐지면서 정렬이 수행되는 것이다.
"""

# 예시 코드
def mergeSort(array):

    # 배열의 요소를 더 이상 좌우로 나눌 수 없을 때
    if len(array) < 2:
        return array

    # 중간 인덱스를 구한다.
    mid = len(array) // 2

    # 배열을 좌우로 나눠 그 배열을 또 나눕니다.
    left = mergeSort(array[mid:])
    right = mergeSort(array[:mid])

    # 좌우를 결합합니다.
    return merge(left, right)


def merge(left, right):

    # 좌, 우가 정렬된 데이터를 저장하는 임시 배열입니다.
    merged = []

    # 좌, 우 배열이 둘다 요소가 존재할 때 까지 반복합니다.
    while len(left) > 0 and len(right) > 0:

        # 가장 작은 첫번째 요소끼리 비교한 후 작은 값은 임시 배열에 추가합니다.
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # 만약 왼쪽 배열이 남아있는 경우 모두 임시 배열에 붙어준다.
    if left:
        merged += left

    # 만약 오른쪽 배열이 남아있는 경우 모두 임시 배열에 붙어준다.
    else:
        merged += right

    return merged

"""
최악과 최선 시간 복잡도가 동일하게 O(NlogN)이다.
logN 의 의미
    N개의 배열이 각각 1개의 원소를 갖는 배열로 쪼개지기까지 logN 번의 과정을 거친다.
N 의 의미
    각 배열의 병합 시, 각 원소를 비교하여 새로운 버퍼에 삽입한다.
    이미 정렬된 두 배열을 합칠때는 버퍼의 크기만큼 N 만큼만 처리를 해준다.
    따라서 배열의 길이인 N 을 곱해준다.
"""

# 퀵 선택 ===========================

"""
동작 순서
    기본적으로 퀵 정렬의 원리를 사용한다.
    배열 중 원하는 값 K가 몇번째로 작은 수 인지 확인할 때 사용한다.
1. 피벗을 선택한 후, 퀵정렬과 동일하게 피벗을 기준으로 정렬한다.
2. 범위에서 정렬이 완료되면, 피벗 값을 기준으로 나뉜다.
    a. 피벗과 K과 동일하면, 정렬 후 피벗 위치의 인덱스를 반환한다.
    b. 피벗이 K보다 크다면, 피벗보다 작은 수들만 추가로 정렬을 시도한다. → 나머지는 버림(정렬 X)
    c. 피벗이 K보다 작다면, 피벗보다 큰 수들만 추가로 정렬을 시도한다. → 나머지는 버림(정렬X)
3. 만약 원소가 1개라면, K와 동일한지 확인
"""

# 예시 코드
import random


def quick_sort(array, start, end, k):

    # 탐색 원소 범위가 1개일경우
    if end - start < 1:
        if k == array[start]:
            print(f"{k}는 {start+1} 번째로 작은 값입니다.")
        return

    pivot = random.randint(start, end)  # 피벗은 랜덤한 인덱스로 선택한다.
    left = start  # 2번째 원소
    right = end  # 마지막 원소까지

    # 랜덤하게 선택된 피벗을 가장 첫 인덱스와 자리를 바꾼다.
    array[left], array[pivot] = array[pivot], array[left]

    while left <= right:

        # 가장 첫 인덱스에 존재하는 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[start]:
            left += 1

        # 가장 첫 인덱스에 존재하는 피벗보다 작은 데이터를 찾을 때까지 반복
        # 시작 인덱스에는 피벗 값이 들어있기 때문에, right의 범위는 start + 1 까지만 가능하다.
        while right > start and array[right] >= array[start]:
            right -= 1

        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        if left <= right:
            array[left], array[right] = array[right], array[left]

    # 구분이 끝난 후, 피벗과 변경해준다.
    array[start], array[right] = array[right], array[start]

    # 만약 k 값이 피벗과 같을 때
    if k == array[right]:
        print(f"{k}는 {right+1} 번째로 작은 값입니다.")

    # 만약 k 값이 피벗보다 작을 때
    elif k < array[right]:
        quick_sort(array, start, right - 1, k)

    # 만약 k 값이 피벗보다 클 때
    elif k > array[right]:
        quick_sort(array, right + 1, end, k)


TEST = list(range(1, 100001))
random.shuffle(TEST)

# 53425는 53425 번째로 작은 값입니다.
quick_sort(TEST, 0, len(TEST) - 1, 53425)

# 정렬 관련 함수 & 메서드 =============================
list = []
boolean = True
sorted(list, reverse = boolean) # 정렬된 리스트를 반환(기존 list는 변화 없음)
list.sort(reverse = boolean) # 리스트를 정렬함

# key 값에 lambda 식을 설정하여 원하는 정렬 조건을 지정
# 예시 1 = 요소의 길이를 기준으로 정렬
list1 = ['test1', 'esttest', '12test']

# 요소의 길이를 기준으로 설정
list1.sort(key=lambda x: len(x))

# ['test1', '12test', 'esttest']
print(list1)

# 예시 2 = 특정 레코드를 기준으로 정렬
list1 = [
	{'name':'Jamie', 'age':35},
	{'name':'Alfredo', 'age':15},
	{'name':'Jessi', 'age':26},
]

# 'name' 레코드를 기준으로 정렬
list1.sort(key=lambda x: x['name'])

# [
#   {'name': 'Alfredo', 'age': 15}, 
#   {'name': 'Jamie', 'age': 35}, 
#   {'name': 'Jessi', 'age': 26}
# ]
print(list1)

# 탐색 관련 개념 ==============================
"""
선형 탐색 & 순차적 탐색 [ O(n) ]
    리스트의 요소들을 처음부터 순차적으로 탐색하여 원하는 값을 찾는 방법이다.
    원하는 값이 발견되지 않을 경우 배열에 있는 모든 원소를 전부 검사한다.
"""

"""
이진 탐색 [ O(logN)]
    크기순으로 정렬된 성질을 이용하기 때문에 이미 정렬되어 있는 배열에서 사용할 수 있는 방법이다.
    배열의 중간의 양옆 값을 확인하여, 원하는 데이터가 어디에 속하는지 점점 좁혀나가는 방법이다.

# 원하는 값이 90
# 원하는 값이 50(1차 탐색 중간 값)보다 큰 상황, 2차 탐색 시 51(lower) ~ 100(upper) 탐색

1 2 3 4 5 ... 47 48 49 50 51 52 53 ... 99 100

# 원하는 값이 75(2차 탐색 중간 값)보다 큰 상황, 2차 탐색 시 75(lower) ~ 100(upper) 탐색
51 52 53 ... 74 75 76 ... 99 100

# 원하는 값이 87 (3차 탐색 중간 값)보다 큰 상황, 2차 탐색 시 87(lower) ~ 100(upper) 탐색
75 76 ... 86 87 88 ... 99 100

... 반복

배열의 크기가 커질수록 동작시간이 기하급수적으로 커지는 선형 탐색 & 순차적 탐색에 비해 이진 탐색 방식은 배열의 크기가 동작시간에 큰 영향을 주지 않는다.
하지만, 이미 정렬된 배열이 우선적으로 필요하기 때문에 일회성으로 사용되는 데이터에서 값을 찾을 때 보다 주기적으로 데이터 탐색이 필요한 데이터 목록에서 사용하면 좋다.
왜냐하면 일회성으로 탐색 후 사용하지 않는 데이터에서 굳이 정렬을 추가로 해줄 필요는 없기 때문이다.
"""

# 예시코드 1 = 반복문을 이용한 탐색, 중간 값보다 타겟이 작을 경우, 왼쪽을 탐색 / 크다면 오른쪽 부분을 탐색한다. start, end 를 조정하며 탐색할 배열의 범위를 조절한다.

def binary_search(array, target):

    start = 0  # 탐색 범위 시작
    end = len(array) - 1  # 탐색 범위 끝

    # 만약 탐색
    while start <= end:

        # 중간 인덱스 구하기
        middle = (start + end) // 2

        # target 값을 찾았을 때
        if array[middle] == target:
            print(f"{target} is {middle} index")
            return

        # 만약 탐색 값이 중간 값보다 크다면
        # 다음 탐색 부분은 중간 인덱스 다음 ~ 마지막 인덱스
        elif array[middle] < target:
            start = middle + 1

        # 만약 탐색 값이 중간 값보다 작다면
        # 다음 탁색 부분은 처음 인덱스 ~ 중간 인덱스 직전
        elif array[middle] > target:
            end = middle - 1

    # 이진 탐색을 마치고도 target 값을 찾지 못했다면
    print(f"Can't search {target} in array")
    return -1

# 예시코드 2 = 재귀를 이용한 탐색, 재귀를 사용하여, 분할 정복 방법으로 탐색할 배열의 범위를 조절한다.

def binary_search(array, target, start, end):

    # 이진 탐색을 마치고도 target 값을 찾지 못했다면
    if start > end:
        print(f"Can't search {target} in array")
        return False

    # 중간 인덱스 구하기
    middle = (start + end) // 2

    # target 값을 찾았을 때
    if array[middle] == target:
        print(f"{target} is {middle} index")

    # 만약 탐색 값이 중간 값보다 크다면
    # 다음 탐색 부분은 중간 인덱스 다음 ~ 마지막 인덱스
    elif array[middle] < target:
        binary_search(array, target, middle + 1, end)

    # 만약 탐색 값이 중간 값보다 작다면
    # 다음 탁색 부분은 처음 인덱스 ~ 중간 인덱스 직전
    elif array[middle] > target:
        binary_search(array, target, start, middle - 1)

    else:
        return False