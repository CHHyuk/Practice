# 큐 자료구조
"""
먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태 
"""

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5) # [5]
queue.append(2) # [5,2]
queue.append(3) # [5,2,3]
queue.append(7) # [5,2,3,7]
queue.popleft() # [2,3,7]
queue.append(1) # [2,3,7,1]
queue.append(4) # [2,3,7,1,4]
queue.popleft() # [3,7,1,4]

print(queue) # [3,7,1,4]
queue.reverse()
print(queue) # [4,1,7,3]