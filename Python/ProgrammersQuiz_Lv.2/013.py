# N개의 최소공배수

def solution(arr):
    result = 1  
    check = 0
    answer = 1
    for i in range(2,max(arr)):
        for j in range(len(arr)):
            if arr[j] % i == 0:
                check += 1
                if check == len(arr):
                    result *= i
        check = 0
    answer = result
    for i in range(len(arr)):
        arr[i] = int(arr[i] / result)
        answer *= arr[i]
    return answer