# 더 맵게 xxxxxxxxxxxxxxxxx

def solution(scoville,k):
    scoville.sort()
    i = 0
    while True:
        if scoville[i] + (scoville[i+1] * 2) < k:
            scoville[i] = scoville[i] + (scoville[i+1] * 2)
            scoville.remove(scoville[i+1])
        elif scoville[i+1] < k:
            scoville[i+1]




solution([1, 2, 3, 9, 10, 12],7)