# 길이가 1부터 10까지인 정사각형의 넓이를 요소로 가지는 리스트
"""
areas = []
for i in range(1,11):
    areas = areas + [i*i]
print(areas)
"""

areas2 = [i*i for i in range(1,11)]
print(areas2)

areas3 = [ i*i for i in range(1,11) if i % 2 == 0 ]
print(areas3)

areas4 = [ ( x, y ) for x in range(15) for y in range(15) ]
print(areas4)