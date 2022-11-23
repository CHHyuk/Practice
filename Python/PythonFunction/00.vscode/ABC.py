X = list(input().split())
A = [1,1,2,2,2,8]
answer_list = []
answer = ''
for i in range(len(X)):
    answer_list.append(A[i]-int(X[i]))
    answer = answer + str(answer_list[i]) + ' '
print(answer)
