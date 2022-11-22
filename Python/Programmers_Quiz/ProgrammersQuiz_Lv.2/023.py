# n^2 배열 자르기 xxxxxxxxxxxxx

def solution(n, left, right):
    temp = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i >= j:
                temp.append(i)
            elif i < j:
                temp.append(j)
    
    temp = temp[left:right+1]
    return temp






solution(3,2,5)