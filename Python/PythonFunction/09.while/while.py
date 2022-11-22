"""
selected = None
while selected not in ['가위','바위','보']: # while문은 selected의 값을 검사해서 그 값(가위, 바위, 보)이 다르면 다시 입력을 받음(반복), 가위,바위,보 중에 값이 입력되면 while문 종료
    selected = input('가위, 바위, 보 중에 선택하세요> ')

print('선택된 값은: ',selected)
"""
patterns = ['가위','바위','보']
for pattern in patterns:
    print(pattern)

patterns = ['가위','바위','보']
for i in range(len(patterns)):
    print(patterns[i]) 

patterns = ['가위','바위','보']
length = len(patterns) # patterns의 길이
i = 0
while i < length: # i가 length보다 작으면
    print(patterns[i])
    i = i + 1