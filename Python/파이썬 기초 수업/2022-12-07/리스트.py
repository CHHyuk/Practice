# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력
list1 = [2,1,5,6,7]
for i in list1:
    print(i)

# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력, len 사용
list2 = [2,1,5,6,7]
for i in range(len(list2)):
    print(list2[i])

# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소들을 역순으로 출력, len 사용
list3 = [2,1,5,6,7]
for i in range(len(list3)):
    print(list3[len(list3)-1-i])

# 문제 : 리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력
list4 = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(len(list4)):
    print('{}월은 {}일까지'.format(i+1,list4[i]))
