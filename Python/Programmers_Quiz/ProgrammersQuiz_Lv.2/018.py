# 행렬의 곱셈 XXXXXXXXXXXX

def solution(arr1, arr2):
    answer = []
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    for i in range(len(arr1)):
        if i == len(arr1)-1:
                break
        for j in range(len(arr2)):
            temp1 = arr1[i]
            temp2 = [arr2[x][j] for x in range(len(temp1))]
            temp3 = [temp1[y] * temp2[y] for y in range(len(temp1))]
            temp4.append(sum(temp3))
            temp1,temp2,temp3 = [],[],[]
        answer.append(temp4)
        temp4 = []
    return answer







solution([[1,2,3,4], [1,2,3,4]],[[1,2], [1,2], [1,2], [1,2]])