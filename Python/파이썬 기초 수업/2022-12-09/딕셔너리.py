ages = [10,20,30]
ages.append(40)

print(ages) # [10, 20, 30, 40]
"""
리스트의 장점
    데이터를 넣을 때 편하다
"""

dict = {
    '철수' : 10,
    '영희' : 20,
    '영수' : 30
}
dict['민희'] = 40

print(dict) # {'철수': 10, '영희': 20, '영수': 30, '민희': 40}
"""
딕셔너리의 장점
    데이터를 가져올 때 편하다
"""
# 버전 1
for name in dict:
  age = dict[name]
  print('{}나이 : {}'.format(name,age))


# 버전 2
for name in dict.keys():
    age = dict[name]
    print('{}나이 : {}'.format(name,age))

# 버전 3
for age in dict.values():
    print('나이 : {}'.format(age))

# 버전 4
for name, age in dict.items():
    print('{}나이: {}'.format(name,age))

del dict['철수'] # 철수 삭제
dict['민희'] = 19 # 민희 나이 19세로 변경

# 버전 4
for name, age in dict.items():
    print('{}나이: {}'.format(name,age))