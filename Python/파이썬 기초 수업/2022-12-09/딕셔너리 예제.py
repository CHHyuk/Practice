# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기
months = {'1월' : 31, '2월' : 28, '3월' : 31, '4월': 30,'5월': 31,'6월' : 30,'7월' : 31,'8월' : 31,'9월':30,'10월' :31,'11월': 30,'12월' : 31}
print(months)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기
date_list = []
for date in months.values():
    date_list.append(date)
print(date_list)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 수작업으로 순회출력
month = {}
for i in range(len(date_list)):
    month[i+1] = date_list[i]

print(month)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, keys()로 key 순회출력
month = {'1월' : 31, '2월' : 28, '3월' : 31, '4월': 30,'5월': 31,'6월' : 30,'7월' : 31,'8월' : 31,'9월':30,'10월' :31,'11월': 30,'12월' : 31}
for key in month.keys():
    print(i)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, keys()로 key, value 순회출력
for key in month.keys():
    date = month[key]
    print('{}은 {}일까지 있음'.format(key,date))

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, values()로 value 순회출력
for value in month.values():
    print(value)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, items()로 key, value 순회출력
for key,value in month.items():
    print('{}은 {}일까지 있음'.format(key,value))

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 3월 정보를 제거
month_del_3 = month
del month_del_3['3월']
print(month_del_3)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 2월을 29일로 수정
month_change_2 = month
month_change_2['2월'] = 29
print(month_change_2)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, update를 이용하여, 2월을 29일로 수정하고 4월, 5월의 정보도 추가
month_update = month
month_update.update({'2월' : 29, '13월' : 30, '14월' : 31})
print(month_update)

# 문제 : 영수, 영희, 철수, 민수의 나이를 딕셔너리에 담기
ages = {}
ages['영수'] = 11
ages['영희'] = 12
ages['철수'] = 13
ages['민수'] = 14
print(ages)

# 문제 : 영수, 영희, 철수, 민수의 나이를 딕셔너리에 담고, 데이터를 넣은 순서대로 순회출력
for key,value in ages.items():
    print(key,'는',value,'살')