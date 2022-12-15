# 큐(Queues)
"""
큐는 데이터를 넣은 순서대로 꺼내서 사용하는 대표적인 FIFO(First In, First Out) 형태의 자료 구조이다.
큐는 데이터를 넣을 때 한 쪽 끝에서 넣어야 하며 꺼낼 때에는 넣은 곳에서 반대 쪽에서 꺼내야한다.
이때 데이터를 넣는 작업을 인큐 연산(enqueue), 데이터를 꺼내는 연산을 디큐 연산(dequeue)이라고 한다.
"""

# 큐에서 만들 수 있는 메소드
"""
size() : 현재 큐에 들어있는 원소의 갯수를 구한다.
isEmpty() : 현재 큐가 빈 큐인지 확인한다. 
"""

# 환형 큐(Circular Queues)
"""
큐의 저장 공간(self.maxCount)을 정한 후, 해당 공간을 돌려가며 사용하는 방식이다.
환형 큐의 저장 공간을 컨트롤하기 위해 Rear(Rear Pointer) 과 Front(Front Pointer) 를 지정하여 사용한다.
"""

#  환형 큐 에서 데이터 추가 & 삭제
"""
환형 큐에서 데이터를 추가할 경우 Rear 을 한칸 움직인 후, 해당 포인트 자리에 데이터를 집어넣는다.
이때 Rear Pointer는 아래와 같은 식을 거쳐 변경된다.

# rear pointer 값이 0 ~ (maxCount-1) 값 범위내에서 이동하기 떄문
rear = (rear + 1) % self.maxCount

환형 큐에서 데이터를 제거할 경우 Front를 한칸 움직인 후, 해당 포인트 자리의 데이터를 제거한다.
이때 Front Pointer는 아래와 같은 식을 거쳐 변경된다.

# front pointer 값이 0 ~ (maxCount-1) 값 범위내에서 이동하기 떄문
front = (front + 1) % self.maxCount
"""

# 우선순위 큐(Priority Queues)
"""
큐의 대표적인 특징인 FIFO(First In, First Out) 를 따르지 않고, 각 원소들의 우선순위를 정하여 해당 우선 순위에 맞춰 데이터를 꺼내는 방식을 사용하는 큐
"""

