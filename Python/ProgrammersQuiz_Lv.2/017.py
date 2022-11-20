# H-Index

def solution(citations):
    result = 0
    citations.sort()
    for i in range(len(citations)):
        if i in citations:
            if citations.count(i) + citations.index(i) >= i:
                result = i
    return result


solution([3, 0, 6, 1, 5])