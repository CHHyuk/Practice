# list.index() = ()값의 위치 찾기
from logging.config import listen


list = [1,2,3,4,5]
print(list.index(2))
# list.extend([value1, value2]) = 리스트 뒤에 value1, value2를 추가
list.extend([6,7])
print(list)
# list.insert(index,value) = 원하는 인덱스 위치에 value값 추가
list.insert(2,1.5)
print(list)
# list.sort() : 값을 순서대로 정렬
list.sort()
print(list)
# list.reverse()
list.reverse()
print(list)