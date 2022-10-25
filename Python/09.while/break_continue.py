# break : 반복문을 종료시키는 기능
# continue : 반복문의 나머지 부분을 보지 않고 반복문의 처음으로 돌아가는 기능
"""
list = [1,2,3,5,7,2,5,237,55]
for a in list:
    if a % 3 == 0:
        print(a)
        break # 3과 237이라는 두개의 값이 출력되어야 하지만 3의 배수인 3을 먼저 찾았으므로 반복문 종료, 3만 출력되게 된다.
"""

list = [1,2,3,5,7,2,5,237,55]

for i in range(10):
    if i%2 !=0:
        print(i)
        print(i)
        print(i)
        print(i)

list = [1,2,3,5,7,2,5,237,55]

for i in range(10):
    if i%2 !=0:
        continue
    print(i)
    print(i)
    print(i)
    print(i)