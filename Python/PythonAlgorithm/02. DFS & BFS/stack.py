# 스택 자료구조
"""
먼저 들어온 데이터가 나중에 나가는 형식(선입후출)
입구와 출구가 동일한 형태
"""
stack = []
stack.append(5) # [5]
stack.append(2) # [5,2]
stack.append(3) # [5,2,3]
stack.append(7) # [5,2,3,7]
stack.pop() # [5,2,3]
stack.append(1) # [5,2,3,1]
stack.append(4) # [5,2,3,1,4]
stack.pop() # [5,2,3,1]

print(stack[::-1]) # 최상단 원소부터 출력, [1,3,2,5]
print(stack) # 최하단 원소부터 출력, [5,2,3,1]
stack.sort()
print(stack)